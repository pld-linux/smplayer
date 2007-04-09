Summary:	smplayer - mplayer frontend
Summary(pl):	smplayer - nak³adka na mplayera
Name:		smplayer
Version:	0.3.13
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://smplayer.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	5408819fc2e2ed902914b631ef73bc52
Patch0:		%{name}-translations_path.patch
URL:		http://smplayer.sourceforge.net/
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	qmake
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

%description -l pl
SMPlayer stara siê byæ kompletn± nak³adk± na MPlayera, pocz±wszy
od podstawowych funkcji jak odtwarzanie plików video, DVD i VCD
koñcz±c na bardziej zaawansowanych opcjach jak obs³uga filtrów
MPlayera oraz wiele wiêcej.

Jedn± z najciekawszych funkcji SMPlayera jest to, ¿e zapamiêtuje
ustawienia wszystkich plików jakie odgrywasz. Zaczynasz ogl±daæ
film, ale musisz wyj¶æ... nie martw siê, kiedy odtworzysz film
ponownie zacznie od momentu, w którym go wy³±czy³e¶ i z tymi
samymi ustawieniami jak: ¶cie¿ka d¼wiêkowa, napisy,
g³o¶no¶æ...

%prep
%setup -q
%patch0 -p0
echo 'CONFIG+= thread' >> src/smplayer.pro
rm -f src/Makefile

%build
export QTDIR=/usr
cd src
qmake
%{__make} \
	DATA_PATH=\\\"/usr/share/smplayer/\\\" \
	CONF_PATH=\\\"/etc/smplayer/\\\"  \
	TRANSLATION_PATH=\\\"/usr/share/smplayer/translations/\\\"  \
	DOC_PATH=\\\"/usr/share/doc/%{name}-%{version}/\\\" \

# "

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
%attr(755,root,root) %{_bindir}/smplayer
%{_desktopdir}/smplayer.desktop
%{_iconsdir}/hicolor/*/apps/smplayer.png
%dir %{_datadir}/smplayer
%{_datadir}/smplayer/input.conf
# icons from 0.3.13
%{_datadir}/smplayer/icons
#
%dir %{_datadir}/smplayer/translations
%lang(de) %{_datadir}/smplayer/translations/smplayer_de.qm
%lang(es) %{_datadir}/smplayer/translations/smplayer_es.qm
%lang(sk) %{_datadir}/smplayer/translations/smplayer_sk.qm
%lang(it) %{_datadir}/smplayer/translations/smplayer_it.qm
%lang(fr) %{_datadir}/smplayer/translations/smplayer_fr.qm
%lang(ru) %{_datadir}/smplayer/translations/smplayer_ru_RU.qm
%lang(zh_CN) %{_datadir}/smplayer/translations/smplayer_zh_CN.qm
%lang(en_US) /usr/share/smplayer/translations/smplayer_en_US.qm
%lang(hu) %{_datadir}/smplayer/translations/smplayer_hu.qm
%lang(ja) %{_datadir}/smplayer/translations/smplayer_ja.qm
%lang(nl) %{_datadir}/smplayer/translations/smplayer_nl.qm
%lang(pl) %{_datadir}/smplayer/translations/smplayer_pl.qm
%lang(uk_UA) %{_datadir}/smplayer/translations/smplayer_uk_UA.qm
