%define	_ver	rc1
Summary:	smplayer - mplayer frontend
Summary(pl.UTF-8):	smplayer - nakładka na mplayera
Name:		smplayer
Version:	0.6.0
Release:	0.%{_ver}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/smplayer/%{name}-%{version}%{_ver}.tar.bz2
# Source0-md5:	f93f6a6840aed0d070c30d1931a62904
URL:		http://smplayer.sourceforge.net/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-linguist >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
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
%setup -q -n %{name}-%{version}%{_ver}

%build
cd src
rm -f Makefile
qmake-qt4
%{__make} \
	THEMES_PATH=\\\"%{_datadir}/smplayer/themes\\\" \
	TRANSLATION_PATH=\\\"%{_datadir}/smplayer/translations/\\\"

lrelease-qt4 smplayer.pro

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

rm -rf $RPM_BUILD_ROOT%{_docdir}/packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog Not_so_obvious_things.txt Readme.txt
%attr(755,root,root) %{_bindir}/smplayer
%{_desktopdir}/smplayer.desktop
%{_iconsdir}/hicolor/*/apps/smplayer.png
%dir %{_datadir}/smplayer
%{_datadir}/smplayer/input.conf
%dir %{_datadir}/smplayer/shortcuts
%{_datadir}/smplayer/shortcuts/default.keys
%dir %{_datadir}/smplayer/translations
%{_mandir}/man1/*
%lang(bg) %{_datadir}/smplayer/translations/smplayer_bg.qm
%lang(cs) %{_datadir}/smplayer/translations/smplayer_cs.qm
%lang(de) %{_datadir}/smplayer/translations/smplayer_de.qm
%lang(en_US) %{_datadir}/smplayer/translations/smplayer_en_US.qm
%lang(el) %{_datadir}/smplayer/translations/smplayer_el_GR.qm
%lang(es) %{_datadir}/smplayer/translations/smplayer_es.qm
%lang(fr) %{_datadir}/smplayer/translations/qt_fr.qm
%lang(fr) %{_datadir}/smplayer/translations/smplayer_fr.qm
%lang(fi) %{_datadir}/smplayer/translations/smplayer_fi.qm
%lang(hu) %{_datadir}/smplayer/translations/smplayer_hu.qm
%lang(it) %{_datadir}/smplayer/translations/smplayer_it.qm
%lang(ja) %{_datadir}/smplayer/translations/smplayer_ja.qm
%lang(ka) %{_datadir}/smplayer/translations/smplayer_ka.qm
%lang(ko) %{_datadir}/smplayer/translations/smplayer_ko.qm
%lang(nl) %{_datadir}/smplayer/translations/smplayer_nl.qm
%lang(pl) %{_datadir}/smplayer/translations/smplayer_pl.qm
%lang(pt) %{_datadir}/smplayer/translations/smplayer_pt_PT.qm
%lang(pt_BR) %{_datadir}/smplayer/translations/smplayer_pt_BR.qm
%lang(ro) %{_datadir}/smplayer/translations/smplayer_ro_RO.qm
%lang(ru) %{_datadir}/smplayer/translations/smplayer_ru_RU.qm
%lang(sk) %{_datadir}/smplayer/translations/smplayer_sk.qm
%lang(sr) %{_datadir}/smplayer/translations/smplayer_sr.qm
%lang(sv) %{_datadir}/smplayer/translations/smplayer_sv.qm
%lang(tr) %{_datadir}/smplayer/translations/smplayer_tr.qm
%lang(uk) %{_datadir}/smplayer/translations/smplayer_uk_UA.qm
%lang(zh_CN) %{_datadir}/smplayer/translations/smplayer_zh_CN.qm
%lang(zh_TW) %{_datadir}/smplayer/translations/smplayer_zh_TW.qm
