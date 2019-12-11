%global pyshortver 37
%global pybasever 3.7
%global pyver %{pybasever}.5
%global pysuffix -infr

Name:       python%{pyshortver}%{pysuffix}
Version:    %{pyver}
Release:    1
Summary:    Python %{pybasever}
License:    PSF
URL:        https://www.python.org

%global _prefix /opt/%{name}
%global debug_package %{nil}
%global _python_bytecompile_errors_terminate_build 0
%global _unpackaged_files_terminate_build 0

BuildRequires: autoconf
BuildRequires: bluez-libs-devel
BuildRequires: bzip2
BuildRequires: bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
 
BuildRequires: findutils
BuildRequires: gcc-c++

BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: gnupg2
BuildRequires: libappstream-glib
BuildRequires: libffi-devel
BuildRequires: libtirpc-devel
BuildRequires: libGL-devel
BuildRequires: libuuid-devel
BuildRequires: libX11-devel
BuildRequires: ncurses-devel
 
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: sqlite-devel
BuildRequires: gdb

BuildRequires: tar
BuildRequires: tcl-devel
BuildRequires: tix-devel
BuildRequires: tk-devel

BuildRequires: xz-devel
BuildRequires: zlib-devel

BuildRequires: /usr/bin/dtrace

BuildRequires: python-rpm-macros

Source0: %{url}/ftp/python/%{pyver}/Python-%{pyver}.tar.xz

Provides: %{name}-%{version}-%{release}
BuildArch: x86_64

%description
Python %{pybasever} for infrastructure needs.

%prep
%setup -q -n Python-%{pyver}
sed -i '1c\#! /usr/bin/env python3' Lib/cgi.py

%build
autoconf
autoheader

%configure	\
		--enable-ipv6 \
		--with-dbmliborder=gdbm \
		--enable-loadable-sqlite-extensions \
		--enable-shared \
		--with-pymalloc \
		--with-computed-gotos=yes
%make_build

%install
%make_install
mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "%{_prefix}/lib64" > %{buildroot}/etc/ld.so.conf.d/%{name}.conf
exit 0

%files
/etc/ld.so.conf.d/python%{pyshortver}%{pysuffix}.conf
%{_prefix}/*
%dir %{_prefix}

%post
ln -sf ../../lib64/python%{pybasever}/lib-dynload %{_prefix}/lib/python%{pybasever}/lib-dynload
ldconfig

%preun
rm -rf %{_prefix}/lib/python%{pybasever}/lib-dynload

%changelog
