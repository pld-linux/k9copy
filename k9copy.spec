Summary:	A vamps frontend
Summary(pl.UTF-8):	Frontend do programu vamps
Name:		k9copy
Version:	1.2.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/k9copy/%{name}-%{version}.tar.gz
# Source0-md5:	7c91b5c58f15330ec668dfccb93e84fb
Patch0:		%{name}-desktop.patch
URL:		http://k9copy.sourceforge.net/
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	libdvdread-devel
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
%setup -q
%patch0 -p1

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

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
%{_datadir}/apps/k9copy
%{_datadir}/apps/konqueror/servicemenus/k9copy_open.desktop
%{_desktopdir}/kde/k9copy.desktop
%{_iconsdir}/*/*x*/*/k9copy.png
