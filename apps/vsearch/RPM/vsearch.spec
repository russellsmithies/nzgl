Name:		vsearch
Version:	1.8.1
Release:	1%{?dist}
Summary:	An alternative to the USEARCH
Group:		Applications/Engineering
License:	GPL3
URL:		https://github.com/torognes/vsearch
Source0: 	vsearch-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	autogen,automake,autoconf

%description
VSEARCH stands for vectorized search, as the tool takes advantage of
parallelism in the form of SIMD vectorization as well as multiple threads to
perform accurate alignments at high speed. VSEARCH uses an optimal global
aligner (full dynamic programming Needleman-Wunsch), in contrast to USEARCH
which by default uses a heuristic seed and extend aligner. This results in more
accurate alignments and overall improved sensitivity (recall) with VSEARCH,
especially for alignments with gaps.

%prep
%setup -q

%build
./autogen.sh
./configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/vsearch %{buildroot}%{_bindir}
install -m 0644 man/vsearch.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/vsearch
%{_mandir}/man1/vsearch.1*

%changelog
* Wed Nov 04 2015 Shane Sturrock <shane@biomatters.com> - 1.8.1
- This release fixes some compatibility issues with older OS X versions as well
  as with QIIME and usearch61.
  - OS X version 10.7 and newer should now be properly supported. 
  - The --threads option will now accept floating point arguments for
    compatibility with usearch61 and QIIME (specifically
    identify_chimeric_seqs.py).

* Wed Oct 21 2015 Shane Sturrock <shane@biomatters.com> - 1.8.0
- Added --search_exact, --fastx_mask and --fastq_convert commands. 
- Changed most commands to read FASTQ input files as well as FASTA files. 
- Modified --fastx_revcomp and --fastx_subsample to also write FASTQ files.

* Mon Oct 19 2015 Shane Sturrock <shane@biomatters.com> - 1.7.0
- Added relabel_keep option

* Mon Oct 12 2015 Shane Sturrock <shane@biomatters.com> - 1.6.0
- Added relabelling options for shuffle and added xsize option for several
  commands.

* Thu Oct 08 2015 Shane Sturrock <shane@biomatters.com> - 1.5.0
- Initial NZGL release
