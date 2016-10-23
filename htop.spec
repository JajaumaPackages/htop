Name:           htop
Version:        2.0.2
Release:        1%{?dist}
Summary:        Interactive process viewer

License:        GPLv2+
URL:            http://hisham.hm/htop/
Source0:        http://hisham.hm/htop/releases/%{version}/htop-%{version}.tar.gz
Patch0:         htop-keywords-trailing-semicolon.patch

BuildRequires:  ncurses-devel
BuildRequires:  desktop-file-utils


%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).


%prep
%setup -q
%patch0 -p1


%build
%configure \
    --enable-openvz \
    --enable-vserver \
    --enable-taskstats \
    --enable-unicode \
    --enable-native-affinity \
    --enable-cgroup \
    --enable-oom

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/htop.desktop


%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/htop
%{_datadir}/pixmaps/htop.png
%{_datadir}/applications/htop.desktop
%{_mandir}/man1/htop.1*


%changelog
* Sun Oct 23 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.0.2-1
- Public release
