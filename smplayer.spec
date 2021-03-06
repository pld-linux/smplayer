# TODO
# - switch to qt5
%define		qtver	4.3.3-3
Summary:	smplayer - mplayer frontend
Summary(pl.UTF-8):	smplayer - nakładka na mplayera
Name:		smplayer
Version:	21.1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	a7e5c8f85e75f9394fe1ce2474d733cd
URL:		http://smplayer.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-linguist >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	rpmbuild(macros) >= 1.596
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	mplayer >= 3:1.0-5.rc2_svn27725.17
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
	QMAKE=qmake-qt4 \
	LRELEASE=lrelease-qt4

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
%doc Changelog Not_so_obvious_things.txt Readme.txt Release_notes.txt
%attr(755,root,root) %{_bindir}/simple_web_server
%attr(755,root,root) %{_bindir}/smplayer
%{_mandir}/man1/smplayer.1*
%{_desktopdir}/smplayer.desktop
%{_desktopdir}/smplayer_enqueue.desktop
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
