cat > mumble-server.spec << 'SPECEOF'
%global debug_package %{nil}

Name:           mumble-server
Version:        1.7.0
Release:        1%{?dist}
Summary:        Mumble VoIP server (murmur)
License:        BSD-3-Clause
URL:            https://mumble.info
Source0:        https://github.com/mumble-voip/mumble.git#master

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  systemd-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-compiler
BuildRequires:  sqlite-devel
BuildRequires:  nlohmann-json-devel
BuildRequires:  spdlog-devel
BuildRequires:  cli11-devel
BuildRequires:  libcap-devel
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  soci-devel >= 4.1.4

Requires:       soci
Requires:       openssl-libs

%description
Mumble is a low-latency, high-quality voice chat application.
This package contains the server component (murmur) only.

%prep
%autosetup -S git -n mumble-master
git submodule update --init --recursive 2>/dev/null || true

%build
cmake -B build -S . \
    -DCMAKE_BUILD_TYPE=Release \
    -Dclient=OFF \
    -Dice=OFF \
    -Denable-postgresql=OFF \
    -Denable-mysql=OFF

cmake --build build %{?_smp_mflags}

%install
cmake --install build --prefix %{buildroot}/usr

%files
%license COPYING
%{_bindir}/murmur
%config(noreplace) %{_sysconfdir}/mumble/in_default.conf

%changelog
* Mon Oct 26 2026 duracellh  - 1.7.0-1
- Initial EPEL 10 build (server only, SQLite3 backend)
SPECEOF
