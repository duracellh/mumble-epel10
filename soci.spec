%global debug_package %{nil}
Name:           soci
Version:        4.1.4
Release:        1%{?dist}
Summary:        C++ database access library
License:        BSD-3-Clause
URL:            https://soci.sourceforge.net/
Source0:        https://github.com/SOCI/soci/archive/refs/heads/release/4.1.tar.gz
BuildRequires:  gcc-c++ cmake sqlite-devel fmt-devel
Requires:       fmt
%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description
SOCI is a lightweight, open source C++ database access library.
%description devel
Development headers and libraries for building applications with SOCI.
%prep
%setup -q -n soci-release-4.1
%build
cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DSOCI_TESTS=OFF -DSOCI_SHARED=ON -DWITH_SQLITE3=ON -DWITH_POSTGRESQL=OFF -DWITH_MYSQL=OFF -DWITH_ODBC=OFF -DWITH_ORACLE=OFF -DWITH_FIREBIRD=OFF -DWITH_DB2=OFF -DWITH_BOOST=OFF
cmake --build build %{?_smp_mflags}
%install
cmake --install build --prefix %{buildroot}/usr
%files
%license LICENSE_1_0.txt
%{_libdir}/libsoci_core.so.*
%{_libdir}/libsoci_sqlite3.so.*
%{_libdir}/libsoci_empty.so.*
%files devel
%{_libdir}/libsoci_core.so
%{_libdir}/libsoci_sqlite3.so
%{_libdir}/libsoci_empty.so
%{_libdir}/cmake/soci-*/
%{_includedir}/soci/
%changelog
* Mon Oct 26 2026 duracellh <zakhuff@gmail.com> - 4.1.4-1
- Initial EPEL 10 build (SQLite3 only)
