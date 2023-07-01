%define		qtver	5.0
Summary:	smplayer - mplayer frontend
Summary(pl.UTF-8):	smplayer - nakładka na mplayera
Name:		smplayer
Version:	23.6.0
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	https://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
Source0:	https://github.com/smplayer-dev/smplayer/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	99f9d40401a395d26904649df9d8576d
URL:		https://www.smplayer.info/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	xorg-lib-libXext-devel
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	mpv >= 0.6.2
Suggests:	smtube
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMPlayer intends to be a complete front-end for MPlayer, from basic
features like playing videos, DVDs, and VCDs to more advanced features
like support for MPlayer filters and more.

One of the most interesting features of SMPlayer: it remembers the
settings of all files you play. So you start to watch a movie but you
have to leave... don't worry, when you open that movie again it will
resume at the same point you left it, and with the same settings:
audio track, subtitles, volume...

%description -l pl.UTF-8
SMPlayer stara się być kompletną nakładką na MPlayera, począwszy od
podstawowych funkcji jak odtwarzanie plików video, DVD i VCD kończąc
na bardziej zaawansowanych opcjach jak obsługa filtrów MPlayera oraz
wiele więcej.

Jedną z najciekawszych funkcji SMPlayera jest to, że zapamiętuje
ustawienia wszystkich plików jakie odgrywasz. Zaczynasz oglądać film,
ale musisz wyjść... nie martw się, kiedy odtworzysz film ponownie
zacznie od momentu, w którym go wyłączyłeś i z tymi samymi
ustawieniami jak: ścieżka dźwiękowa, napisy, głośność...

%prep
%setup -q

# skip docs install
%{__sed} -i -e '/DOC_PATH/d' Makefile src/smplayer.pro

# skip manpage compress
%{__sed} -i -e '/gzip/d' Makefile

# skip build rule on install
%{__sed} -i -e 's,install: src/smplayer,install:,' Makefile

# disable debug on console on unix too
%{__sed} -i -e '/NO_DEBUG_ON_CONSOLE/s,#DEFINES,DEFINES,' src/smplayer.pro

%build
%{__make} \
	PREFIX=%{_prefix} \
	QMAKE=qmake-qt5 \
	LRELEASE=lrelease-qt5

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/smplayer/themes
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Readme.txt README.md Release_notes.md
%attr(755,root,root) %{_bindir}/simple_web_server
%attr(755,root,root) %{_bindir}/smplayer
%{_mandir}/man1/smplayer.1*
%{_desktopdir}/smplayer.desktop
%{_desktopdir}/smplayer_enqueue.desktop
%{_datadir}/metainfo/smplayer.appdata.xml
%{_iconsdir}/hicolor/*/apps/smplayer.png
%{_iconsdir}/hicolor/*/apps/smplayer.svg
%dir %{_datadir}/smplayer
%{_datadir}/smplayer/input.conf
%dir %{_datadir}/smplayer/shortcuts
%{_datadir}/smplayer/shortcuts/default.keys
%{_datadir}/smplayer/shortcuts/euskara.keys
%{_datadir}/smplayer/shortcuts/vlc.keys
%dir %{_datadir}/smplayer/themes
%dir %{_datadir}/smplayer/translations
