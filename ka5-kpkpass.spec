%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kpkpass
Summary:	kpkpass
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0a9f867aa3ba9373e96db932fe2d3aec
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to deal with Apple Wallet pass files. Apple Wallet files are
essentially ZIP files containing a JSON description of the pass,
translated message catalogs and graphical assets to render the pass.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
/etc/xdg/org_kde_kpkpass.categories
%attr(755,root,root) %ghost %{_libdir}/libKPimPkPass.so.5
%attr(755,root,root) %{_libdir}/libKPimPkPass.so.5.*.*
%{_datadir}/mime/packages/application-vnd-apple-pkpass.xml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim/KPkPass
%{_libdir}/cmake/KPimPkPass
%attr(755,root,root) %{_libdir}/libKPimPkPass.so
