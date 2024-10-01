Name:           choose
Version:        1.3.5
Release:        1%{?dist}
Summary:        A human-friendly and fast alternative to cut and (sometimes) awk

License:        MIT
URL:            https://github.com/theryangeary/choose
Source0:        https://github.com/theryangeary/choose/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gzip
BuildRequires:  upx

%description
A longer description of your package

%global debug_package %{nil}

%prep
%setup -q

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release
strip --strip-all target/release/%{name}
upx target/release/%{name}

%install
mkdir -p %{buildroot}/%{_bindir}
upx target/release/%{name}
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Tue Oct 1 2024 - Danie de Jager - 1.3.4-5
* Fri Sep 13 2024 - Danie de Jager - 1.3.4-5
* Tue May 21 2024 - Danie de Jager - 1.3.4-4
* Fri Apr 26 2024 - Danie de Jager - 1.3.4-3
* Thu Apr 11 2024 - Danie de Jager - 1.3.4-2
* Fri Mar 22 2024 - Danie de Jager - 1.3.4-1
