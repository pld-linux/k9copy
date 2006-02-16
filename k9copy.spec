Summary:	A vamps frontend
Name:		k9copy
Version:	1.0.3b
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://k9copy.free.fr/file.php?file=%{name}-%{version}.tar.gz
# Source0-md5:	1eef6d87ff3cf91594c1a32615356cd0
URL:		http://k9copy.free.fr/
BuildRequires:	dvdauthor
BuildRequires:	kdelibs-devel
BuildRequires:	libdvdcss
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread
BuildRequires:	libstdc++-devel
BuildRequires:	m4
BuildRequires:	vamps
Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	libdvdcss
Requires:	ibdvdnav
Requires:	libdvdread
Requires:	vamps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
k9copy is a very easy-to-use GUI for vamps that allows the shrinking
of DVDs from DVD 9 to DVD 5 under KDE in Linux

%package devel
Summary:	Header files for k9copy library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel

%description devel
Header files for libk3bcore library.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	manprefix=%{_mandir}

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libk9copy.so.0.0.0
#%{_desktopdir}/k9copy.desktop
%{_iconsdir}/hicolor/48x48/apps/k9copy.png
%{_datadir}/apps/k9copy/k9copyui.rc

%files devel
%defattr(644,root,root,755)
%{_libdir}/libk9copy.la
%{_includedir}/*.h
