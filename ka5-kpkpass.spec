%define		kdeappsver	21.08.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kpkpass
Summary:	kpkpass
Name:		ka5-%{kaname}
Version:	21.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b654668ed2b326ca4e2d6d9ce5eb891f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	ninja
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

%description -l pl.UTF-8
Biblioteka do obsługi portfela Apple z plikami haseł. Pliki Apple
Wallet są plikami ZIP z JSONowym opisem pass, a także katalogiem z
tłumaczeniami i plikami graficznymi.

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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/libKPimPkPass.so.5
%attr(755,root,root) %{_libdir}/libKPimPkPass.so.*.*.*
%{_datadir}/mime/packages/application-vnd-apple-pkpass.xml
%{_datadir}/qlogging-categories5/org_kde_kpkpass.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim/KPkPass
%{_libdir}/cmake/KPimPkPass
%{_libdir}/libKPimPkPass.so
