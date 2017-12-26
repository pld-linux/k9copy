#
# Conditional build:
%bcond_with	qt5		# build with Qt5 and KDE5
#
Summary:	A vamps frontend
Summary(pl.UTF-8):	Frontend do programu vamps
Name:		k9copy
Version:	3.0.3
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/k9copy-reloaded/%{name}-%{version}.tar.gz
# Source0-md5:	53158282e23a4aa4fb8f4336f1424521
Patch0:		%{name}-desktop.patch
Patch1:		cxx.patch
Patch2:		ffmpeg3.patch
Patch3:		qt5.patch
Patch4:		kde4api.patch
URL:		http://k9copy-reloaded.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	automoc4
BuildRequires:	ffmpeg-devel
BuildRequires:	libdvdread-devel
BuildRequires:	mpeg2dec-devel
BuildRequires:	xine-lib-devel
%if %{with qt5}
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdelibs4support
BuildRequires:	kf5-kdesu-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kpty-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	qt5-build
%else
BuildRequires:	kde4-kdelibs-devel >= 4.1.0
BuildRequires:	qt4-build
%endif
Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	vamps
Obsoletes:	k9copy-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
k9copy is a very easy-to-use GUI for vamps that allows the shrinking
of DVDs from DVD 9 to DVD 5 under KDE in Linux.

%description -l pl.UTF-8
k9copy to bardzo łatwy w użyciu graficzny interfejs do programu vamps,
umożliwiający zmniejszanie obrazów płyt DVD z DVD 9 do DVD 5 w
środowisku KDE pod Linuksem.

%prep
%setup -q -c -T
%{__tar} xmf %{SOURCE0}
%{__mv} k9copy/* .
%patch1 -p1
%patch2 -p1
%if %{with qt5}
%patch3 -p1
%else
%patch4 -p1
%endif

%build
install -d build
cd build
%cmake \
	%{?with_qt5:-DQT5_BUILD:BOOL=ON} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	kde_htmldir=%{_kdedocdir} \
	manprefix=%{_mandir}

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%if %{with qt5}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/adown.png
%{_datadir}/%{name}/anim.mng
%{_datadir}/%{name}/aright.png
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/k9copyui.rc
%{_datadir}/%{name}/mencoder.xml
%{_desktopdir}/k9copy.desktop
%{_desktopdir}/k9copy_assistant.desktop
%{_datadir}/solid/actions/k9copy_assistant_open.desktop
%{_datadir}/solid/actions/k9copy_open.desktop
%else
%{_datadir}/apps/k9copy
%{_desktopdir}/kde4/k9copy.desktop
%{_desktopdir}/kde4/k9copy_assistant.desktop
%{_datadir}/apps/solid/actions/k9copy_assistant_open.desktop
%{_datadir}/apps/solid/actions/k9copy_open.desktop
%endif
%{_iconsdir}/*/*x*/*/k9copy.png
