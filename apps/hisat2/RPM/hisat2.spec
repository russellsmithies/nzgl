Name:		hisat2
Version:	2.1.0
Release:	1%{?dist}
Summary:	A fast and sensitive alignment program for mapping NGS reads
Group:		Applications/Bioinformatics
License:	GPL 3.0
URL:		https://ccb.jhu.edu/software/hisat2/index.shtml
Source0:	ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-%{version}-source.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	bowtie2 python27

%description

HISAT2 is a fast and sensitive alignment program for mapping next-generation
sequencing reads (whole-genome, transcriptome, and exome sequencing data) to a
population of human genomes (as well as to a single reference genome). Based on
an extension of BWT for a graph [1], we designed and implemented a graph FM
index (GFM), an original approach and its first implementation to the best of
our knowledge. In addition to using one global GFM index that represents
general population, HISAT2 uses a large set of small GFM indexes that
collectively cover the whole genome (each index representing a genomic region
of 56 Kbp, with 55,000 indexes needed to cover human population). These small
indexes (called local indexes) combined with several alignment strategies
enable effective alignment of sequencing reads. This new indexing scheme is
called Hierarchical Graph FM index (HGFM). We have developed HISAT2 based on
the HISAT [2] and Bowtie 2 [3] implementations. See the HISAT2 website for more
information.

%prep
%setup -q
find . -type f -name '*.py' | xargs sed 's=python=python2.7=g' --in-place
find . -type f -name '*genotype*.py' | xargs sed "/ sys,/a sys.path.append('/usr/libexec/hisat2/hisatgenotype_modules')" --in-place

%build
make clean
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
/bin/cp -r scripts %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r doc %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r example %{buildroot}/%{_libexecdir}/%{name}/
install -m 0755 extract_exons.py %{buildroot}%{_bindir}
install -m 0755 extract_splice_sites.py %{buildroot}%{_bindir}
install -m 0755 hisat2 %{buildroot}%{_bindir}
install -m 0755 hisat2-align-l %{buildroot}%{_bindir}
install -m 0755 hisat2-align-s %{buildroot}%{_bindir}
install -m 0755 hisat2-build %{buildroot}%{_bindir}
#install -m 0755 hisat2_build_genotype_genome.py %{buildroot}%{_bindir}
install -m 0755 hisat2-build-l %{buildroot}%{_bindir}
install -m 0755 hisat2-build-s %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_exons.py %{buildroot}%{_bindir}
#install -m 0755 hisat2_extract_HLA_vars.py %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_snps_haplotypes_UCSC.py %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_snps_haplotypes_VCF.py %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_splice_sites.py %{buildroot}%{_bindir}
#install -m 0755 hisat2_genotype.py %{buildroot}%{_bindir}
install -m 0755 hisat2-inspect %{buildroot}%{_bindir}
install -m 0755 hisat2-inspect-l %{buildroot}%{_bindir}
install -m 0755 hisat2-inspect-s %{buildroot}%{_bindir}
install -m 0755 hisat2_simulate_reads.py %{buildroot}%{_bindir}
#install -m 0755 hisat2_test_BRCA_genotyping.py %{buildroot}%{_bindir}
#install -m 0755 hisat2_test_HLA_genotyping.py %{buildroot}%{_bindir}
install -m 0755 hisatgenotype_build_genome.py %{buildroot}%{_bindir}
install -m 0755 hisatgenotype_extract_reads.py %{buildroot}%{_bindir}
install -m 0755 hisatgenotype_extract_vars.py %{buildroot}%{_bindir}
install -m 0755 hisatgenotype_hla_cyp.py %{buildroot}%{_bindir}
install -m 0755 hisatgenotype_locus.py %{buildroot}%{_bindir}
install -m 0755 hisatgenotype.py %{buildroot}%{_bindir}
#install -m 0755 old_hisat2_test_HLA_genotyping.py %{buildroot}%{_bindir}
/bin/cp -r hisatgenotype_scripts %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r hisatgenotype_modules %{buildroot}/%{_libexecdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE MANUAL NEWS TUTORIAL VERSION
/usr/bin/extract_exons.py
/usr/bin/extract_splice_sites.py
/usr/bin/hisat2
/usr/bin/hisat2-align-l
/usr/bin/hisat2-align-s
/usr/bin/hisat2-build
#/usr/bin/hisat2_build_genotype_genome.py
/usr/bin/hisat2-build-l
/usr/bin/hisat2-build-s
/usr/bin/hisat2_extract_exons.py
#/usr/bin/hisat2_extract_HLA_vars.py
/usr/bin/hisat2_extract_snps_haplotypes_UCSC.py
/usr/bin/hisat2_extract_snps_haplotypes_VCF.py
/usr/bin/hisat2_extract_splice_sites.py
#/usr/bin/hisat2_genotype.py
/usr/bin/hisat2-inspect
/usr/bin/hisat2-inspect-l
/usr/bin/hisat2-inspect-s
/usr/bin/hisat2_simulate_reads.py
#/usr/bin/hisat2_test_BRCA_genotyping.py
#/usr/bin/hisat2_test_HLA_genotyping.py
/usr/bin/hisatgenotype_build_genome.py
/usr/bin/hisatgenotype_extract_reads.py
/usr/bin/hisatgenotype_extract_vars.py
/usr/bin/hisatgenotype_hla_cyp.py
/usr/bin/hisatgenotype_locus.py
/usr/bin/hisatgenotype.py
#/usr/bin/old_hisat2_test_HLA_genotyping.py
/usr/libexec/%{name}/*

%changelog
* Mon Jun 12 2017 Shane Sturrock <shane.sturrock@nzgenomics.com> - 2.1.0-1
- This major version includes the first release of HISAT-genotype, which
  currently performs HLA typing, DNA fingerprinting analysis, and CYP typing on
  whole genome sequencing (WGS) reads. We plan to extend the system so that it
  can analyze not just a few genes, but a whole human genome. Please refer to 
  the HISAT-genotype website for more details.
- HISAT2 can be directly compiled and executed on Windows system using Visual
  Studio, thanks to Nigel Dyer.
- Implemented --new-summary option to output a new style of alignment summary,
  which is easier to parse for programming purposes.
- Implemented --summary-file option to output alignment summary to a file in
  addition to the terminal (e.g. stderr).
- Fixed discrepancy in HISAT2’s alignment summary.
- Implemented --no-templatelen-adjustment option to disable automatic template
  length adjustment for RNA-seq reads.

* Mon Nov 07 2016 Shane Sturrock <shane@biomatters.com> - 2.0.5-1
- Due to a policy change (HTTP to HTTPS) in using SRA data (--sra-option),
  users are strongly encouraged to use this version. As of 11/9/2016, NCBI will
  begin a permanent redirect to HTTPS, which means the previous versions of
  HISAT2 no longer works with --sra-acc option soon.
- Implemented -I and -X options for specifying minimum and maximum fragment
  lengths. The options are valid only when used with --no-spliced-alignment,
  which is used for the alignment of DNA-seq reads.
- Fixed some cases where reads with SNPs on their 5' ends were not properly
  aligned.
- Implemented --no-softclip option to disable soft-clipping.
- Implemented --max-seeds to specify the maximum number of seeds that HISAT2
  will try to extend to full-length alignments (see the manual for details).

* Tue Aug 16 2016 Shane Sturrock <shane@biomatters.com> - 2.0.4-1
- Initial release of Hisat2 for BioIT
- Scripts, doc and examples can be found in /usr/libexec/hisat2
