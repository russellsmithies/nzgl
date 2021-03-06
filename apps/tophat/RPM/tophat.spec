%define samtools_version 0.1.18

Name:		tophat
Version:	2.1.1
Release:	1%{?dist}
Summary:	A spliced read mapper for RNA-Seq
Group:		Applications/Engineering
License:	Artistic 2.0
URL:		http://tophat.cbcb.umd.edu/
Source0:	http://tophat.cbcb.umd.edu/downloads/tophat-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	boost >= 1.47
BuildRequires:	boost-devel >= 1.47
BuildRequires:	boost-thread >= 1.47
BuildRequires:	boost-jam >= 1.47
BuildRequires:	boost-math >= 1.47
BuildRequires:	boost-random >= 1.47
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
Requires:	bowtie2

%description

TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns
RNA-Seq reads to mammalian-sized genomes using the ultra
high-throughput short read aligner Bowtie, and then analyzes the
mapping results to identify splice junctions between exons.

TopHat is a collaborative effort between the University of Maryland
Center for Bioinformatics and Computational Biology and the University
of California, Berkeley Departments of Mathematics and Molecular and
Cell Biology.

%prep
%setup -q

%build
LDFLAGS='-lboost_thread-mt' ./configure --prefix=/usr
# Do not build if smp_mflags used
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/bam2fastx %{buildroot}%{_bindir}
install -m 0755 src/bam_merge %{buildroot}%{_bindir}
install -m 0755 src/bed_to_juncs %{buildroot}%{_bindir}
#install -m 0755 src/closure_juncs %{buildroot}%{_bindir}
install -m 0755 src/contig_to_chr_coords %{buildroot}%{_bindir}
install -m 0755 src/fix_map_ordering %{buildroot}%{_bindir}
install -m 0755 src/gtf_juncs %{buildroot}%{_bindir}
install -m 0755 src/gtf_to_fasta %{buildroot}%{_bindir}
install -m 0755 src/juncs_db %{buildroot}%{_bindir}
install -m 0755 src/long_spanning_reads %{buildroot}%{_bindir}
install -m 0755 src/map2gtf %{buildroot}%{_bindir}
install -m 0755 src/prep_reads %{buildroot}%{_bindir}
install -m 0755 src/sam_juncs %{buildroot}%{_bindir}
install -m 0755 src/samtools_0.1.18 %{buildroot}%{_bindir}
install -m 0755 src/segment_juncs %{buildroot}%{_bindir}
install -m 0755 src/sra_to_solid %{buildroot}%{_bindir}
install -m 0755 src/tophat %{buildroot}%{_bindir}
install -m 0755 src/tophat2 %{buildroot}%{_bindir}
install -m 0755 src/tophat-fusion-post %{buildroot}%{_bindir}
install -m 0755 src/tophat_reports %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README AUTHORS LICENSE THANKS
%{_bindir}/*

%changelog
* Fri Feb 26 2016 Shane Sturrock <shane@biomatters.com> - 2.1.1-1
- Please note that TopHat has entered a low maintenance, low support stage as
  it is now largely superseded by HISAT2 which provides the same core
  functionality (i.e. spliced alignment of RNA-Seq reads), in a more accurate 
  and much more efficient way.
- TopHat can be now built on more recent Linux distributions with newer GNU C++
  (5.x), as the included SeqAn library was finally upgraded to a newer version.
- improved the detection of linker options for the Boost::Thread library which
  prevented the TopHat build from source on some systems.
- incorporated Luca Venturini's code to support large bowtie2 indexes (.bt2l).
- bam2fastx usage message (-h/--help) was updated in order to better document
  the functions of this program which can be used as a standalone utility for
  converting reads from BAM/SAM to FASTQ/FASTA; the -v/--version option was 
  also added to this utility for easier integration in other pipelines.

* Wed Jul 01 2015 Shane Sturrock <shane@biomatters.com> - 2.1.0-1
- TopHat-Fusion algorithm improvements for more sensitive and accurate 
  discovery of fusions, thanks to contributions from Gordon Bean and Ryan 
  Kelley at Illumina.
- This release implements a new algorithm for counting fusion-supporting read 
  pairs that reduces the number of false-positive potential fusions. This 
  algorithm computes the inner distance between read pairs by first converting 
  the pair positions to transcript coordinates using the transcript information
  in refGene.txt and ensGene.txt. Pairs with small inner distance (suggesting 
  the pair could come from a plausible pair-end insert) are counted as 
  supporting evidence for the fusion. The default threshold for the inner 
  distance is 250 base pairs; this parameter can be set using the 
  --fusion-pair-dist <int> flag.
- fixed a few issues with GFF parsing of some annotation files
- fixed a runtime-error when using --no-discordant option.
- Several fixes/improvements thanks to contributors on GitHub:
  - new --max-num-fusions option allowing the user to specify the maximum 
    number of reported fusions in tophat-fusion-post
  - adjusting lower limit for --fusion-multipairs
  - fixed a few typos, cleaning up python code etc.

* Thu Mar 26 2015 Shane Sturrock <shane@biomatters.com> - 2.0.14-1
- pipeline speed improvements thanks to contributions from Véronique Legrand 
  and Michaël Pressigout of Institut Pasteur
- added support for xz compressed read files (thanks to a patch submitted by 
  Ashton Trey Belew)
- applied a couple of Python fixes to prevent potential issues with package 
  handling and some file operations
- fixed a potential linking issue where the wrong libbam.a library could have 
  been linked when building from source

* Fri Oct 03 2014 Shane Sturrock <shane@biomatters.com> - 2.0.13-1
- removed SAMtools as an external dependency in order to avoid incompatibility 
  issues with recent and future changes of SAMtools and its code library (an 
  older, stable SAMtools version is now packaged with TopHat)
- fixed a few code compatibility issues when compiling on OSX 10.9

* Fri Jul 04 2014 Sidney Markowitz <sidney@biomatters.com> - 2.0.12-1
- Fix from upstream to accommodate changed option in new version of bowtie2

* Wed Jun 11 2014 Sidney Markowitz <sidney@biomatters.com> - 2.0.11-2
- NZGL patch to accommodate changed option in new version of bowtie2

* Wed Mar 05 2014 Shane Sturrock <shane@biomatters.com> - 2.0.11-1
- Version 2.0.11 is a maintenance release with the following simple fix:
  This version is compatible with Bowtie2 v2.2.1, although it does not 
  support a 64-bit Bowtie2 index yet.

* Fri Nov 15 2013 Shane Sturrock <shane@biomatters.com> - 2.0.10-1
- Improved support for adding unpaired reads to PE reads in the same TopHat2 
  run (please see the manual entry for this usage). This includes reporting 
  separate counts for the additional unpaired reads and making sure that the 
  SAM flags in the output files reflect the paired or unpaired origin of the 
  reads.
- Added the possibility to run TopHat just for the purpose of preparing the 
  transcriptome index files (please see the manual entry for this special 
  usage).
- The input read files can have different file formats, as TopHat now 
  autodetects the FASTA/FASTQ format of each input file.
- Fixed a bug that could sometimes incorrectly rename the reads in the output 
  alignments.
- The stats in align_summary.txt now reflect the reported mappings under the 
  constraints of the provided Tophat options, instead of reflecting the 
  internally detected alignments. As such, the number of reads with multiple 
  mappings may appear to be incorrectly reported if the user provided options 
  that directly affect the reporting of such multiple mapppings.
- Fixed a bug that caused TopHat to fail when bowtie1 and pre-filtering options
  were used together.

* Fri Aug 30 2013 Shane Sturrock <shane@biomatters.com> - 2.0.10-1
- New upstream release - no changelog

* Mon Jul 01 2013 Shane Sturrock <shane@biomatters.com> - 2.0.9-1
- New upstream release

* Wed May 15 2013 Shane Sturrock <shane@biomatters.com> - 2.0.8b-1
- New upstream release fixing bowtie version check errors

* Mon Feb 25 2013 Carl Jones <carl@biomatters.com> - 2.0.8-0
- New upstream release

* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 2.0.7-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 2.0.6-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 2.0.5-1
- New upstream release
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 2.0.4-3
- Fix license details
- Fix Requires 
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 2.0.4-2
- Fix compilation issues
* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 2.0.4-1
- New upstream release
* Thu Aug 11 2011 Adam Huffman <bloch@verdurin.com> - 1.3.1-1
- initial version
