%global debug_package %{nil}

Name:           mumble-server
Version:        1.7.0
Release:        1%{?dist}
Summary:        Mumble VoIP server (murmur)
License:        BSD-3-Clause
URL:            https://www.mumble.info
Source0:        https://github.com/mumble-voip/mumble.git#master

BuildRequires:  gcc-c++ cmake
BuildRequires:  systemd-rpm-macros
BuildRequires:  git
BuildRequires:  systemd-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  protobuf-devel protobuf-compiler
BuildRequires:  systemd-rpm-macros
BuildRequires:  libcap-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  nlohmann-json-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  spdlog-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  cli11-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  soci-devel >= 4.1.4
BuildRequires:  systemd-rpm-macros

Requires:       soci
Requires:       openssl-libs

%description
Mumble is a low-latency, high-quality voice chat application.
This package contains only the server component (murmur).

%prep
%autosetup -q -n mumble-master
git submodule update --init --recursive 2>/dev/null || true

%build
cmake -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -Dclient=OFF \
    -Dice=OFF \
    -Denable-postgresql=OFF \
    -Denable-mysql=OFF \
    -DCMAKE_INSTALL_PREFIX=/usr

cmake --build build %{?_smp_mflags}

%install
cmake --install build --prefix %{buildroot}/usr

%files
%license COPYING
/usr/bin/mumble-server
/usr/bin/mumble-server-user-wrapper
%config(noreplace) /usr/etc/mumble/mumble-server.ini
/usr/share/man/man1/mumble-server.1
/usr/share/man/man1/mumble-server-user-wrapper.1
/usr/etc/sysusers.d/mumble-server.conf
/usr/etc/tmpfiles.d/mumble-server.conf
/usr/etc/systemd/system/mumble-server.service

%changelog
* Mon Oct 26 2026 duracellh <zakhuff@gmail.com> - 1.7.0-1
- Initial EPEL 10 build (server only, SQLite3 backend)
