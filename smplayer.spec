%define		qtver	4.3.3-3
Summary:	smplayer - mplayer frontend
Summary(pl.UTF-8):	smplayer - nakładka na mplayera
Name:		smplayer
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	e39ba5b54e6218d411ecd296002d77bb
URL:		http://smplayer.sourceforge.net/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-linguist >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	desktop-file-utils
Requires:	mplayer >= 3:1.0-5.rc2_svn27725.17
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

# skip docs isntall
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc Changelog Not_so_obvious_things.txt Readme.txt
%attr(755,root,root) %{_bindir}/smplayer
%dir %{_datadir}/smplayer
%{_datadir}/smplayer/input.conf
%dir %{_datadir}/smplayer/shortcuts
%{_datadir}/smplayer/shortcuts/default.keys
%dir %{_datadir}/smplayer/themes
%dir %{_datadir}/smplayer/translations
%lang(ar) %{_datadir}/smplayer/translations/smplayer_ar_SY.qm
%lang(bg) %{_datadir}/smplayer/translations/smplayer_bg.qm
%lang(ca) %{_datadir}/smplayer/translations/smplayer_ca.qm
%lang(cs) %{_datadir}/smplayer/translations/smplayer_cs.qm
%lang(de) %{_datadir}/smplayer/translations/smplayer_de.qm
%lang(en_US) %{_datadir}/smplayer/translations/smplayer_en_US.qm
%lang(el) %{_datadir}/smplayer/translations/smplayer_el_GR.qm
%lang(es) %{_datadir}/smplayer/translations/smplayer_es.qm
%lang(et) %{_datadir}/smplayer/translations/smplayer_et.qm
%lang(eu) %{_datadir}/smplayer/translations/smplayer_eu.qm
%lang(fi) %{_datadir}/smplayer/translations/smplayer_fi.qm
%lang(fr) %{_datadir}/smplayer/translations/smplayer_fr.qm
%lang(gl) %{_datadir}/smplayer/translations/smplayer_gl.qm
%lang(hu) %{_datadir}/smplayer/translations/smplayer_hu.qm
%lang(it) %{_datadir}/smplayer/translations/smplayer_it.qm
%lang(ja) %{_datadir}/smplayer/translations/smplayer_ja.qm
%lang(ka) %{_datadir}/smplayer/translations/smplayer_ka.qm
%lang(ko) %{_datadir}/smplayer/translations/smplayer_ko.qm
%lang(ku) %{_datadir}/smplayer/translations/smplayer_ku.qm
%lang(lt) %{_datadir}/smplayer/translations/smplayer_lt.qm
%lang(mk) %{_datadir}/smplayer/translations/smplayer_mk.qm
%lang(nl) %{_datadir}/smplayer/translations/smplayer_nl.qm
%lang(pl) %{_datadir}/smplayer/translations/smplayer_pl.qm
%lang(pt) %{_datadir}/smplayer/translations/smplayer_pt.qm
%lang(pt_BR) %{_datadir}/smplayer/translations/smplayer_pt_BR.qm
%lang(ro) %{_datadir}/smplayer/translations/smplayer_ro_RO.qm
%lang(ru) %{_datadir}/smplayer/translations/smplayer_ru_RU.qm
%lang(sk) %{_datadir}/smplayer/translations/smplayer_sk.qm
%lang(sl) %{_datadir}/smplayer/translations/smplayer_sl_SI.qm
%lang(sr) %{_datadir}/smplayer/translations/smplayer_sr.qm
%lang(sv) %{_datadir}/smplayer/translations/smplayer_sv.qm
%lang(tr) %{_datadir}/smplayer/translations/smplayer_tr.qm
%lang(uk) %{_datadir}/smplayer/translations/smplayer_uk_UA.qm
%lang(vi) %{_datadir}/smplayer/translations/smplayer_vi_VN.qm
%lang(zh_CN) %{_datadir}/smplayer/translations/smplayer_zh_CN.qm
%lang(zh_TW) %{_datadir}/smplayer/translations/smplayer_zh_TW.qm
%{_desktopdir}/smplayer.desktop
%{_desktopdir}/smplayer_enqueue.desktop
%{_iconsdir}/hicolor/*/apps/smplayer.png
%{_mandir}/man1/smplayer.1*
