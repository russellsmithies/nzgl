Name:		bamtools
Version:	2.4.1
Release:	1%{?dist}
Summary:	Tools for handing BAM files
Group:		Applications/Engineering
License:	MIT
URL:		https://github.com/pezmaster31/bamtools
Source0:	https://github.com/downloads/pezmaster31/bamtools/bamtools-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake
BuildRequires:	zlib-devel

%description
BamTools provides both a programmer's API and an end-user's toolkit for handling
BAM files.

%prep
%setup -q

%build
mkdir build
cd build
cmake ..
make
cd ..

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -m 0755 bin/bamtools-%{version} %{buildroot}%{_bindir}/bamtools
/bin/cp -a lib/* %{buildroot}%{_libdir}
/bin/cp -a include/* %{buildroot}%{_includedir}
cd %{buildroot}%{_libdir}
ln -sf libbamtools.so.%{version} libbamtools.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/bamtools
%{_libdir}/*
%{_includedir}/*

%changelog
* Wed Dec 14 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> 2.4.1-1
- Added: list-tag support to 'bamtools split'
- Fixed: various architecture/compiler errors (see commits for specifics)
- Fixed: documentation-related errors

* Thu Jun 18 2015 Shane Sturrock <shane@biomatters.com> 2.4.0-1
- Minor version bump
  - Added support for custom header tags.
  - Suppressed clang compiler warnings.

* Tue Jul 22 2014 Shane Sturrock <shane@biomatters.com> 2.3.0-1
- Long overdue update due to watch script not working
- No changelog published by author

* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> 1.0.2-2
- Fix libbamtools.so symlink

* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> 1.0.2-1
- Initial build.
