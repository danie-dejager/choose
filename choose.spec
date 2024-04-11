Name:           choose
Version:        1.3.4
Release:        2%{?dist}
Summary:        A human-friendly and fast alternative to cut and (sometimes) awk

License:        MIT
URL:            https://github.com/theryangeary/choose
Source0:        https://github.com/theryangeary/choose/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  upx

%description
A longer description of your package

%global debug_package %{nil}

%prep
%setup -q

%build
cargo build --release 

%install
mkdir -p %{buildroot}/%{_bindir}
upx target/release/%{name}
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Thu Apr 11 2024 Danie de Jager - 1.3.4-2
* Fri Mar 22 2024 Danie de Jager - 1.3.4-1
