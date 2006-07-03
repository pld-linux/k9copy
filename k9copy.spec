%define _rc     beta1
Summary:	A vamps frontend
Summary(pl):	Frontend do programu vamps
Name:		k9copy
Version:	1.1.0
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/k9copy/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	d9918b924ba4e42fdfbfa139ff899198
URL:		http://k9copy.free.fr/
Patch0:		%{name}-desktop.patch
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	libdvdread-devel
Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	vamps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
k9copy is a very easy-to-use GUI for vamps that allows the shrinking
of DVDs from DVD 9 to DVD 5 under KDE in Linux.

%description -l pl
k9copy to bardzo ³atwy w u¿yciu graficzny interfejs do programu vamps,
umo¿liwiaj±cy zmniejszanie obrazów p³yt DVD z DVD 9 do DVD 5 w
¶rodowisku KDE pod Linuksem.

%package devel
Summary:	Header files for k9copy library
Summary(pl):	Pliki nag³ówkowe biblioteki k9copy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel >= 9:3.0

%description devel
Header files for libk3bcore library.

%description devel -l pl
Pliki nag³ówkowe biblioteki k9copy.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
%patch0 -p0

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir},%{_desktopdir}/kde}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	kde_htmldir=%{_kdedocdir} \
	manprefix=%{_mandir}
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Multimedia/k9copy.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libk9copy.so.*.*.*
%{_datadir}/apps/k9copy
%{_datadir}/apps/konqueror/servicemenus/k9copy_open.desktop
%{_desktopdir}/kde/k9copy.desktop
%{_iconsdir}/*/*x*/*/k9copy.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libk9copy.so
%{_libdir}/libk9copy.la
%{_includedir}/*.h
