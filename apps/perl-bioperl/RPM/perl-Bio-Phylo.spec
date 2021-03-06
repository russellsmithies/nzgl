Name:           perl-Bio-Phylo
Version:        0.50
Release:        1%{?dist}
Summary:        Phylogenetic analysis using perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Bio-Phylo/
Source0:        http://www.cpan.org/authors/id/R/RV/RVOSA/Bio-Phylo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is the base class for the Bio::Phylo package for phylogenetic analysis
using object-oriented perl5. In this file, methods are defined that are
performed by other objects in the Bio::Phylo release that inherit from this
base class (which you normally wouldn't use directly).

%prep
%setup -q -n Bio-Phylo-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

#%check
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING LICENSE README.txt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 05 2012 Carl Jones <carl@biomatters.com> 0.50-1
- Specfile autogenerated by cpanspec 1.78.
