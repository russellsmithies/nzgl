Name:		fastq_screen
Version:	0.11.1
Release:	1%{?dist}
Summary:	Contamination screening for next-gen sequence data

Group:		Applications/Engineering
License:	GPLv3+
URL:		http://www.bioinformatics.bbsrc.ac.uk/projects/%{name}/
Source0:	http://www.bioinformatics.bbsrc.ac.uk/projects/%{name}/%{name}_v%{version}.tar.gz
Source1:	%{name}-README.Fedora
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	bowtie

%description

FastQ Screen provides a simple way to screen a library of short reads
against a set of reference libraries. Its most common use is as part
of a QC pipeline to confirm that a library comes from the expected
source, and to help identify any sources of contamination.

%prep
%setup -q -n %{name}_v%{version}

cp -p %{SOURCE1} .

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 %{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}.conf

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt RELEASE_NOTES.txt fastq_screen-README.Fedora
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}


%changelog
* Fri Feb 24 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 0.11.1-1
- Fixed bug preventing selection of --filter options 4 or 5
- Added --filter options 4 and 5
- Added option --pass to further improve filtering
- Prevented HTML bar graphs overlapping when screening against multiple genomes
- Corrected documentation describing how to use the option --top

* Mon Jan 23 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 0.10.0-1
- Added option --top for faster processing, when speed of processing is the
  highest priority
- Improve appearance of HTML graphs

* Fri Dec 09 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 0.9.5-1
- Fixed bug causing FastQ Screen, when running in --bisulfite mode, to mislabel
  species names in the HTML bisulfite read orientation graph on the occasion
  that one or more of the samples tested contained reads that mapped to none of
  the bisulfite converted reference genomes

* Tue Nov 22 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 0.9.4-1
- New colour scheme which should be easily interpretable by colour blind people
- Fixed bug preventing, in some instances, genome names being displayed in the
  header line of filtered (using the --filter option) FASTQ files

* Wed Nov 02 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 0.9.3-1
- v0.9.3 is a minor release.
- Fixed bug stopping the command-line --threads option overriding 
  the configuration file. 
- When the --tag option was specified, FastQ Screen should have 
  analysed all the reads in a file by default. However, a bug resulted
  in a subset file being generated and analysed instead. This has been
  fixed and now a reduced reads file will only be generated with the 
  --tag option if explicitly requested using the --subset command.
- Fixed bug causing FastQ Screen to not process reads containing 
  full-stop in the FASTQ read header.  
- Changes to what is reported when using the --quiet option
- Updated documentation.

* Thu Oct 13 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 0.9.2-1
- When --outdir option selected, FastQ Screen creates the output directory if
  it does not already exist.
- FastQ Screen in bisulfite mode checks whether the bisulfite orientation graph
  already exists.
- Adjusted how compressed files are read to improve compatibility with Mac
  systems.
- Fixed bug causing the HTML report to be missing one genome when reporting
  conventional (i.e. not bisulfite) alignment results
- Updated documentation.

* Fri Oct 07 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 0.9.1-1
- Fixed bug causing FastQ Screen to terminate prematurely when in 
  bisulfite mode if no reads map to a bisulfite reference genome.

* Wed Oct 05 2016 Shane Sturrock <shane@biomatters.com> - 0.9.0-1
- FastQ Screen, when run in Bisulfite mode, reports to which strand the reads
  aligned (original top strand, complementary to original top strand,
  complementary to original bottom strand, or original bottom strand).

* Mon Sep 12 2016 Shane Sturrock <shane@biomatters.com> - 0.8.0-1
- Program is now compatible with aligner BWA
- FastQ Screen produces an HTML summary report
- Program documentation has been substantially updated and is now in Markdown
  format

* Tue Aug 02 2016 Shane Sturrock <shane@biomatters.com> - 0.7.0-1
- Added --tag option to create output FASTQ files in which the the genomes to
  which a read maps is appended to the first line of the FASTQ read
- Added --filter option to extract reads from a tagged FASTQ file which map, or
  do not map, to a specified combination of genomes
- Pre-existing option --nohits is now equivalent to the parameters --tag
  --filter 000 (number of zeroes corresponds to the number of genome being
  screened)

* Thu Jul 14 2016 Shane Sturrock <shane@biomatters.com> - 0.6.4-1
- Program no longer terminates if a single Bismark reference genome index is
  incorrectly specified
- Fixed bug causing program to crash if --aligner bowtie2 and --bisulfite
  specified together
- FastQ Screen can now use Bowtie (in addition to Bowtie2) when performing
  Bisulfite mapping with Bismark
- Fixed bug in how FastQ Screen checks for dependencies (e.g. SamTools)

* Fri Jul 08 2016 Shane Sturrock <shane@biomatters.com> - 0.6.3-1
- Fixed bug causing --subset 0 to crash
- Fixed bug in which the reported percentage reads mapping to no libraries was,
  in some instances, an underestimate of the correct value

* Mon Jul 06 2016 Shane Sturrock <shane@biomatters.com> - 0.6.2-1
- Updated help text
- Refactored code

* Mon Jul 04 2016 Shane Sturrock <shane@biomatters.com> - 0.6.1-1
- Fixed bug causing program to crash in some instances when --outdir option
  selected

* Tue Jun 28 2016 Shane Sturrock <shane@biomatters.com> - 0.6.0-1
- Compatible with Bismark, enabling bisulfite library QC
- Option --colorspace is no longer supported

* Tue Sep 08 2015 Shane Sturrock <shane@biomatters.com> - 0.5.2-1
- Fixed bug observed when --nohits option selected causing initialization
  warnings, in some instances

* Wed Jul 15 2015 Shane Sturrock <shane@biomatters.com> - 0.5.1-1
- Ensures a FASTQ file is not mapped against the same library more than 
  once

* Wed Jul 01 2015 Shane Sturrock <shane@biomatters.com> - 0.5.0-1
- Please note that users no longer need to specify whether a genome 
  index is compatible with bowtie or bowtie2, since this is now 
  determined automatically.
- Option --subset 100000 is now the default.  Use --subset 0 to 
  process an entire file (not recommended for most QC applications, 
  since this generally takes much more time). 
- Option --paired removed.
- Bowtie2 is now the default aligner, replacing the orignal bowtie.
- New option --force instructs fastq_screen to overwrite extant output 
  files.
- The script now uses a more memory efficient internal data structure
  for recording which reads map to what library. However, this means
  that a maximum of 15 libraries may be specified with 32-bit Perl
  or 31 libraries with 64-bit Perl.

* Thu Jul 10 2014 Sidney Markowitz <sidney@biomatters.com> - 0.4.4-1
- Fix a bug in check for the presence of bowtie2 indices for large genomes.
- Add a nicer font for the graph and improved some of the colours
- Fixed output file naming for file names ending with .fq and .gz.

* Wed Jun 04 2014 Sidney Markowitz <sidney@biomatters.com> - 0.4.3-1
- Upstream release v0.4.3 fixed bug causing all reads to be written
  to the 'no hits' output file when using Bowtie2 as the aligner.
- Bowtie2 now runs with the parameters '--no-discordant' and
  '--no-mixed' when mapping paired-end reads.
- The 'nohits' output file has the file extension '.fastq' and
  is compressed if the input files are compressed.
- rpm spec change - upstream changed name of example conf file

- v0.4.2 is a minor release. The script no longer defaults to 
  Bowtie if "--aligner" is not specified.  Instead, the script checks 
  the configuration file to determine if Bowtie/Bowtie2 paths and 
  indices  have been specified. If both Bowtie and Bowtie2 indices 
  have been specified, FastqScreen then defaults to the original 
  Bowtie. The script now reports the number of reads mapping each 
  genome in addition to percentages.

* Wed Jun 26 2013 Shane Sturrock <shane@biomatters.com> - 0.4.1-1
- New upstream release

* Thu Dec 13 2012 Carl Jones <carl@biomatters.com> - 0.4-1
- New upstream release

* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 0.3.1-1
- New upstream release

* Wed Aug 10 2011 Adam Huffman <bloch@verdurin.com> - 0.2.1-2
- add README explaining use of fastq_screen.conf

* Fri Aug  5 2011 Adam Huffman <bloch@verdurin.com> - 0.2.1-1
- initial version

