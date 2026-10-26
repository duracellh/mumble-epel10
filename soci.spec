%global debug_package %{nil}

Name:           soci
Version:        4.1.4
Release:        1%{?dist}
Summary:        C++ database access library
License:        BSD-3-Clause
URL:            https://soci.sourceforge.net/
Source0:        https://github.com/SOCI/soci/archive/refs/heads/release/4.1.tar.gz   

BuildRequires:  gcc-c++ cmake
BuildRequires:  sqlite-devel

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description
SOCI is a lightweight, open source C++ database access library.

%description devel
Development headers and libraries for building applications with SOCI.

%prep
%setup -q -n soci-%{version}

%build
cmake -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DSOCI_TESTS=OFF \
    -DSOCI_SHARED=ON \
    -DWITH_SQLITE3=ON \
    -DWITH_POSTGRESQL=OFF \
    -DWITH_MYSQL=OFF \
    -DWITH_ODBC=OFF \
    -DWITH_ORACLE=OFF \
    -DWITH_FIREBIRD=OFF \
    -DWITH_DB2=OFF \
    -DWITH_BOOST=OFF

cmake --build build -j%{?_smp_mflags}

%install
cmake --install build --prefix %{buildroot}/usr

%files
%license LICENSE
%{_libdir}/libsoci_core.so.*
%{_libdir}/libsoci_sqlite3.so.*
%{_libdir}/libsoci_empty.so.*
%{_includedir}/soci/

%files devel
%{_libdir}/libsoci_core.so
%{_libdir}/libsoci_sqlite3.so
%{_libdir}/libsoci_empty.so
%{_libdir}/cmake/soci-*/
%{_includedir}/soci/sqlite3/
%{_includedir}/soci/empty/

%changelog
* Mon Oct 26 2026 Your Name <you@example.com> - 4.1.4-1
- Initial EPEL 10 build (SQLite3 only)   
