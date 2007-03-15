Summary:	smplayer
Summary(pl.UTF-8):	smplayer
Name:		smplayer
Version:	0.2.26
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://smplayer.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	3af1fe4698f6286d2adc05de1593ce9f
URL:		http://smplayer.sourceforge.net/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMPlayer intends to be a complete front-end for MPlayer, from basic features like playing videos, DVDs, and VCDs to more advanced features like support for MPlayer filters and more. 

One of the most interesting features of SMPlayer: it remembers the settings of all files you play. So you start to watch a movie but you have to leave... don't worry, when you open that movie again it will resume at the same point you left it, and with the same settings: audio track, subtitles, volume...

#%description -l pl.UTF-8

%prep
%setup -q

%build
cd src/
rm -f Makefile
qt3to4 -alwaysOverwrite %{name}.pro
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	KDE_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	CONF_PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
