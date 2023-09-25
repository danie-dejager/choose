Name:           choose
Version:        1.3.4
Release:        1%{?dist}
Summary:        A human-friendly and fast alternative to cut and (sometimes) awk
BuildRequires:  upx

License:        MIT
URL:            https://github.com/theryangeary/choose
Source0:        %{name}-%{version}.tar.gz

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
