Summary:	A vamps frontend
Summary(pl.UTF-8):	Frontend do programu vamps
Name:		k9copy
Version:	2.3.6
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/k9copy/%{name}-%{version}-Source.tar.gz
# Source0-md5:	c062dcb141a0320afe9dae0d36f87965
Patch0:		%{name}-desktop.patch
URL:		http://k9copy.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	hal-devel
BuildRequires:	kde4-kdelibs-devel >= 4.1.0
BuildRequires:	libdvdread-devel
BuildRequires:	mpeg2dec-devel
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
%setup -q -n %{name}-%{version}-Source

%build
install -d build
cd build
%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -LCMS_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
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
%{_datadir}/apps/k9copy
%{_desktopdir}/kde4/k9copy.desktop
%{_desktopdir}/kde4/k9copy_assistant.desktop
%{_datadir}/apps/solid/actions/k9copy_assistant_open.desktop
%{_datadir}/apps/solid/actions/k9copy_open.desktop
%{_iconsdir}/*/*x*/*/k9copy.png
