# TODO
# - smtube: use system qtsingleapplication

%define		qtver	4.3.3-3
%define		smver	14.8.0
Summary:	smplayer - mplayer frontend
Summary(pl.UTF-8):	smplayer - nakładka na mplayera
Name:		smplayer
Version:	15.11.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	e6f459f640908df2403381a39a27cdba
Source1:	http://downloads.sourceforge.net/smplayer/smtube-%{smver}.tar.bz2
# Source1-md5:	21d9341a1a5de13a7064296f6625d399
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
Suggests:	%{name}-smtube
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

%package smtube
Summary:	Support for youtube videos
Summary(pl.UTF-8):	Wparcie dla filmów youtube
License:	GPL
Group:		X11/Applications

%description smtube
Support for youtube videos in smplayer.

%description smtube -l pl.UTF-8
Wparcie dla filmów youtub dla aplikacji smplaer.

%prep
%setup -q -a1
mv smtube-%{smver} smtube

# skip docs install
%{__sed} -i -e '/DOC_PATH/d' Makefile src/smplayer.pro
%{__sed} -i -e '/DOC_PATH/d' Makefile smtube/src/smtube.pro

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

%{__make} -C smtube \
	PREFIX=%{_prefix} \
	QMAKE=qmake-qt4 \
	LRELEASE=lrelease-qt4

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/smplayer/themes
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C smtube install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/smtube

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc Changelog Not_so_obvious_things.txt Readme.txt Release_notes.txt
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
%dir %{_datadir}/smplayer/themes
%dir %{_datadir}/smplayer/translations
%lang(ar) %{_datadir}/smplayer/translations/smplayer_ar.qm
%lang(ar_SY) %{_datadir}/smplayer/translations/smplayer_ar_SY.qm
%lang(bg) %{_datadir}/smplayer/translations/smplayer_bg.qm
%lang(ca) %{_datadir}/smplayer/translations/smplayer_ca.qm
%lang(cs) %{_datadir}/smplayer/translations/smplayer_cs.qm
%lang(da) %{_datadir}/smplayer/translations/smplayer_da.qm
%lang(de) %{_datadir}/smplayer/translations/smplayer_de.qm
%lang(el) %{_datadir}/smplayer/translations/smplayer_el_GR.qm
%lang(en_GB) %{_datadir}/smplayer/translations/smplayer_en_GB.qm
%lang(en_US) %{_datadir}/smplayer/translations/smplayer_en_US.qm
%lang(es) %{_datadir}/smplayer/translations/smplayer_es.qm
%lang(et) %{_datadir}/smplayer/translations/smplayer_et.qm
%lang(eu) %{_datadir}/smplayer/translations/smplayer_eu.qm
%lang(fi) %{_datadir}/smplayer/translations/smplayer_fi.qm
%lang(fr) %{_datadir}/smplayer/translations/smplayer_fr.qm
%lang(gl) %{_datadir}/smplayer/translations/smplayer_gl.qm
%lang(he_IL) %{_datadir}/smplayer/translations/smplayer_he_IL.qm
%lang(hr) %{_datadir}/smplayer/translations/smplayer_hr.qm
%lang(hu) %{_datadir}/smplayer/translations/smplayer_hu.qm
%lang(id) %{_datadir}/smplayer/translations/smplayer_id.qm
%lang(it) %{_datadir}/smplayer/translations/smplayer_it.qm
%lang(ja) %{_datadir}/smplayer/translations/smplayer_ja.qm
%lang(ka) %{_datadir}/smplayer/translations/smplayer_ka.qm
%lang(ko) %{_datadir}/smplayer/translations/smplayer_ko.qm
%lang(ku) %{_datadir}/smplayer/translations/smplayer_ku.qm
%lang(lt) %{_datadir}/smplayer/translations/smplayer_lt.qm
%lang(mk) %{_datadir}/smplayer/translations/smplayer_mk.qm
%lang(ms_MY) %{_datadir}/smplayer/translations/smplayer_ms_MY.qm
%lang(nl) %{_datadir}/smplayer/translations/smplayer_nl.qm
%lang(nn) %{_datadir}/smplayer/translations/smplayer_nn_NO.qm
%lang(pl) %{_datadir}/smplayer/translations/smplayer_pl.qm
%lang(pt) %{_datadir}/smplayer/translations/smplayer_pt.qm
%lang(pt_BR) %{_datadir}/smplayer/translations/smplayer_pt_BR.qm
%lang(ro) %{_datadir}/smplayer/translations/smplayer_ro_RO.qm
%lang(ru) %{_datadir}/smplayer/translations/smplayer_ru_RU.qm
%lang(sk) %{_datadir}/smplayer/translations/smplayer_sk.qm
%lang(sl) %{_datadir}/smplayer/translations/smplayer_sl_SI.qm
%lang(sq_AL) %{_datadir}/smplayer/translations/smplayer_sq_AL.qm
%lang(sr) %{_datadir}/smplayer/translations/smplayer_sr.qm
%lang(sv) %{_datadir}/smplayer/translations/smplayer_sv.qm
%lang(th) %{_datadir}/smplayer/translations/smplayer_th.qm
%lang(tr) %{_datadir}/smplayer/translations/smplayer_tr.qm
%lang(uk) %{_datadir}/smplayer/translations/smplayer_uk_UA.qm
%lang(uz) %{_datadir}/smplayer/translations/smplayer_uz.qm
%lang(vi) %{_datadir}/smplayer/translations/smplayer_vi_VN.qm
%lang(zh_CN) %{_datadir}/smplayer/translations/smplayer_zh_CN.qm
%lang(zh_TW) %{_datadir}/smplayer/translations/smplayer_zh_TW.qm

%files smtube
%defattr(644,root,root,755)
%doc smtube/{Readme.txt,Release_notes.txt,Changelog}
%attr(755,root,root) %{_bindir}/smtube
%{_desktopdir}/smtube.desktop
%{_iconsdir}/hicolor/*/apps/smtube.png
%dir %{_datadir}/smtube
%dir %{_datadir}/smtube/translations
%lang(ar) %{_datadir}/smtube/translations/smtube_ar.qm
%lang(bg) %{_datadir}/smtube/translations/smtube_bg.qm
%lang(ca) %{_datadir}/smtube/translations/smtube_ca.qm
%lang(cs) %{_datadir}/smtube/translations/smtube_cs.qm
%lang(de) %{_datadir}/smtube/translations/smtube_de.qm
%lang(el) %{_datadir}/smtube/translations/smtube_el.qm
%lang(en) %{_datadir}/smtube/translations/smtube_en.qm
%lang(en_GB) %{_datadir}/smtube/translations/smtube_en_GB.qm
%lang(es) %{_datadir}/smtube/translations/smtube_es.qm
%lang(et) %{_datadir}/smtube/translations/smtube_et.qm
%lang(eu) %{_datadir}/smtube/translations/smtube_eu.qm
%lang(fi) %{_datadir}/smtube/translations/smtube_fi.qm
%lang(fr) %{_datadir}/smtube/translations/smtube_fr.qm
%lang(gl) %{_datadir}/smtube/translations/smtube_gl.qm
%lang(he_IL) %{_datadir}/smtube/translations/smtube_he_IL.qm
%lang(hr) %{_datadir}/smtube/translations/smtube_hr.qm
%lang(hu) %{_datadir}/smtube/translations/smtube_hu.qm
%lang(id) %{_datadir}/smtube/translations/smtube_id.qm
%lang(it) %{_datadir}/smtube/translations/smtube_it.qm
%lang(ja) %{_datadir}/smtube/translations/smtube_ja.qm
%lang(ka) %{_datadir}/smtube/translations/smtube_ka.qm
%lang(ko) %{_datadir}/smtube/translations/smtube_ko.qm
%lang(lt) %{_datadir}/smtube/translations/smtube_lt.qm
%lang(ms_MY) %{_datadir}/smtube/translations/smtube_ms_MY.qm
%lang(nn_NO) %{_datadir}/smtube/translations/smtube_nn_NO.qm
%lang(nqo) %{_datadir}/smtube/translations/smtube_nqo.qm
%lang(pl) %{_datadir}/smtube/translations/smtube_pl.qm
%lang(pt) %{_datadir}/smtube/translations/smtube_pt.qm
%lang(pt_BR) %{_datadir}/smtube/translations/smtube_pt_BR.qm
%lang(ru) %{_datadir}/smtube/translations/smtube_ru_RU.qm
%lang(sk) %{_datadir}/smtube/translations/smtube_sk.qm
%lang(sq_AL) %{_datadir}/smtube/translations/smtube_sq_AL.qm
%lang(sr) %{_datadir}/smtube/translations/smtube_sr.qm
%lang(sv) %{_datadir}/smtube/translations/smtube_sv.qm
%lang(tr) %{_datadir}/smtube/translations/smtube_tr.qm
%lang(uk) %{_datadir}/smtube/translations/smtube_uk.qm
%lang(vi) %{_datadir}/smtube/translations/smtube_vi.qm
%lang(zh_CN) %{_datadir}/smtube/translations/smtube_zh_CN.qm
%lang(zh_TW) %{_datadir}/smtube/translations/smtube_zh_TW.qm
