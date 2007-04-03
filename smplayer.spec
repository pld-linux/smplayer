Summary:	smplayer - mplayer frontend
Summary(pl.UTF-8):	smplayer - nakładka na mplayera
Name:		smplayer
Version:	0.3.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://smplayer.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	e5cc291295a201fc9fcff12898f58875
URL:		http://smplayer.sourceforge.net/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	mplayer
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
SMPlayer stara się być kompletną nakładką na MPlayera, począwszy
od podstawowych funkcji jak odtwarzanie plików video, DVD i VCD
kończąc na bardziej zaawansowanych opcjach jak obsługa filtrów
MPlayera oraz wiele więcej.

Jedną z najciekawszych funkcji SMPlayera jest to, że zapamiętuje
ustawienia wszystkich plików jakie odgrywasz. Zaczynasz oglądać
film, ale musisz wyjść... nie martw się, kiedy odtworzysz film
ponownie zacznie od momentu, w którym go wyłączyłeś i z tymi
samymi ustawieniami jak: ścieżka dźwiękowa, napisy,
głośność...

%prep
%setup -q

%build
cd src
rm -f Makefile
qt3to4 -alwaysOverwrite %{name}.pro
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}/ \
	KDE_PREFIX=$RPM_BUILD_ROOT%{_prefix}/ \
	CONF_PREFIX=$RPM_BUILD_ROOT%{_prefix}/
rm -rf $RPM_BUILD_ROOT%{_docdir}/packages
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog Not_so_obvious_things.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/smplayer.desktop
%{_iconsdir}/hicolor/*/apps/smplayer.png
%dir %{_datadir}/smplayer
%{_datadir}/smplayer/input.conf
%dir %{_datadir}/smplayer/translations
%lang(de) %{_datadir}/smplayer/translations/smplayer_de.qm
%lang(en_US) %{_datadir}/smplayer/translations/smplayer_en_US.qm
%lang(es) %{_datadir}/smplayer/translations/smplayer_es.qm
%lang(sk) %{_datadir}/smplayer/translations/smplayer_sk.qm
%lang(it) %{_datadir}/smplayer/translations/smplayer_it.qm
%lang(fr) %{_datadir}/smplayer/translations/smplayer_fr.qm
%lang(hu) %{_datadir}/smplayer/translations/smplayer_hu.qm
%lang(pl) %{_datadir}/smplayer/translations/smplayer_pl.qm
%lang(ru) %{_datadir}/smplayer/translations/smplayer_ru_RU.qm
%lang(zh_CN) %{_datadir}/smplayer/translations/smplayer_zh_CN.qm
