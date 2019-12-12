Name:       carbonapi
Version:    1.0
Release:    2
Summary:    CarbonAPI
License:    BSD-2

Source0:    %{name}-%{version}.tar.gz
Source1:    %{name}.service

Requires:   cairo, systemd-units
Requires(post): systemd
Requires(preun):  systemd
Requires(postun): systemd

Provides:   %{name}-%{version}-%{release}

BuildArch:  x86_64


%description
CarbonAPI - replacement graphite API server.

%prep
%setup -q -n carbonapi

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -rfa * %{buildroot}/opt/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}

%files
%dir /opt/%{name}
%dir /opt/%{name}/bin
%dir /opt/%{name}/conf
/opt/%{name}/bin/carbonapi
%config(noreplace) /opt/%{name}/conf/config.yaml
%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog