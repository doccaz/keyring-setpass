#
# spec file for package keyring-setpass
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           keyring-setpass
Version:        1.0
Release:        0
Summary:	Deletes and recreates the keyring without a password
License:        SUSE-NonFree
Group:          Productivity/System/Utilities
Url:            http://suportelinux.df.bb.com.br/svn/autoyast/pacotes/keyring-setpass
Source:         %{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This utility deletes the login keyring and recreates it without a password.
Temporary workaround for externally changed AD passwords.

%prep
%setup -q

%build
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
install -m 755 bin/Release/keyring-setpass %{buildroot}%{_bindir}/
install -m 644 keyring-setpass.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/keyring-setpass
%{_sysconfdir}/xdg/autostart/keyring-setpass.desktop

%changelog

