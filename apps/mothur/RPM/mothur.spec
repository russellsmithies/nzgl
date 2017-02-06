Name:		mothur
Version:	1.39.1
Release:	1%{?dist}
Summary:	Computational microbial ecology tool
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.mothur.org/w/images/b/bc/Mothur.%{version}.zip
Source0:	mothur-%{version}.tar.gz
patch0:		makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	readline-devel ncurses-devel gcc-gfortran glibc-static

%description
The mothur project was initiated by Dr. Patrick Schloss and his
software development team in the Department of Microbiology &
Immunology at The University of Michigan. This project seeks to
develop a single piece of open-source, expandable software to fill the
bioinformatics needs of the microbial ecology community. The authors
have incorporated the functionality of dotur, sons, treeclimber,
s-libshuff, unifrac, and much more. In addition to improving the
flexibility of these algorithms, they have added a number of other
features including calculators and visualization tools.

%prep
#Deal with mistakenly included OS X files
%setup -q   -n mothur-%{version}
rm -rf __MACOSX* .DS_Store
%patch0 -p0

%build
#makefile doesn't support SMP builds
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Mon Feb 06 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 1.39.1-1
- Bug Fixes:
  - pre.cluster (without groups) not clustering properly. #301
  - make.contigs fixes "off by one" name mismatch error. #303
  - rename.file unable to automatically rename with output directory specified.
  - cluster and cluster.split improper printing of list file when using name
    file option. Does not effect printing of the list file when clustered with
    count file.
  - cluster and cluster.split improper printing of list file when using phylip
    file option. Does not effect printing of the list file when clustered with
    column file.
  - Incorrect taxlevel printed in *.tax.summary file.

* Thu Jan 26 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 1.39.0-1
- Feature Updates
 - Changes default clustering method to opti.
 - Adds agc and dgc vsearch clustering methods for Windows users. #215
 - Adds chimera.vsearch command for Windows users. #215
 - Major speed improvement for pre.cluster command with aligned files. #220
 - Major memory requirement reduction for pre.cluster command with by group
   option. #220
 - Adds constaxonomy file to current files saved by mothur.
 - Control-C handling: In script or batch mode exit mothur. In interactive mode
   exit command. #212
http://www.mothur.org/forum/viewtopic.php?f=5&t=4102&p=12431#p12431
 - Adds blastdir parameter to set.dir command. #223
 - Taxonomy files can now contain spaces in the taxon names. #265
 - Makes refasta and repnames parameters optional for create.database command.
   #32
 - Removes cutoff adjust in dist.seqs command. #274
 - Adds trim parameter to make.sra command for use with sff files.
- Bug Fixes
 - Fixes Windows multiple processors with groups crash - chimera.uchime
   command.
 - Fixes Windows bug with make.file command. #255
 - Creates unique group names for 3 column format make.file command. #270
 - Fixes bug with number of "taxon"_unclassifeds appended to taxonomy in
   classify.seqs.
 - Eliminates zero abundance OTUs created by some floating point biom files
   converted to shared files make.shared.
 - Floating point exception in sparcc command.
 - Fixes bug where mothur was not finding matches for sequence names "off by
   one character" in the name. make.contigs
 - Fixes bug with "find" command for Linux user in make.file
 - Fixes bug with optimize parameter using alignreport file in screen.seqs
   command. #288

* Thu Aug 11 2016 Shane Sturrock <shane@biomatters.com> - 1.38.1.1-1
- New Commands
  - merge.count command combines count files. #259
- Feature Updates
  - Removes hard parameter from cluster, cluster.classic and cluster.split
    commands. All commands now use hard=T.
  - Improved help command. #257
  - Make.file command is more flexible with filenames. #243
  - Adds prefix parameter to Make.file command. #251
  - Changes bad character in group names error to warning. Modifies group names
    with '-' characters in output filenames to avoid downstream issues.
- Bug Fixes
  - Fixes bug with output directory in make.group command.
  - Fixes filename expansion issue make.contigs.
  - Fixes group name issue with oligos file option in get.mimarkspackage
    command.

* Thu Jul 21 2016 Shane Sturrock <shane@biomatters.com> - 1.38.1-1
- New Commands
  - rename.file - renames file and updates current files saved by mothur.
  - chimera.vsearch - detects chimeras using vsearch software package. #239
- Feature Updates
  - Removes hcluster command. It is really really slow and we don't recommend
    it. #208
  - Removes save option which kept references in memory. #208
  - Removes clear.memory command which worked with the save option. #208
  - Removes pds.pipeline command. #208
  - Command line mode returns exit-code to indicate failure. #151
  - Removes reftaxonomy parameter from classify.otu and summary.tax. #241
  - Removes large parameter from count.seqs command. #203
  - Allows make.biom with picrust option to handle mothur's new
    parentTaxon_unclassified format. #241
  - Adds mothur's location as a default file location to check. Reduces unable
    to open file errors. #231
  - Adds count parameter to sens.spec command. #225
  - Clarifies seq.error command output. #175
  - Adds sets parameter to lefse command. #234
  - Removes indexFile requirement for using NONE option in oligos file.
    make.contigs. #193
  - make.contigs command will skip blank file pairs. #233
  - Warn about illegal characters in group names to prevent downstream analysis
    issues. #37
  - Adds rdiffs to pcr.seqs command to allow for setting different diffs for
    the forward and reverse primers. #244
- Bug Fixes
  - Mothur can handle whitespace in command lines. #191
  - Fixes gradient bar on heatmap.sim command. #237
  - Fixes bug with classify.otu persample option.
  - Fixes bug with agc method in cluster and cluster.split
  - Fixes bug with summary.tax command not including name file counts in
    *tax.summary.
  - Fixes RAM output for linux get.current. #232
  - Error generated when filenames are too long for uchime program. #226
  - Fixes cutoff adjust for agc and dgc clustering methods. #254

* Wed Jun 22 2016 Shane Sturrock <shane@biomatters.com> - 1.37.6-1
- Fixes make.contigs gz file error.

* Mon Jun 13 2016 Shane Sturrock <shane@biomatters.com> - 1.37.5-1
- Fixes file divide bug with make.contigs for certain sequence name types.

* Mon May 16 2016 Shane Sturrock <shane@biomatters.com> - 1.37.4-1
- Fixes chimera.uchime size= instead of ab= for datasets run without references
  or groups.

* Wed May 04 2016 Shane Sturrock <shane@biomatters.com> - 1.37.3-1
- Fixes bug with agc and dgc methods in the cluster.split and cluster commands
  that added one duplicate names to OTUs.

* Wed Apr 20 2016 Shane Sturrock <shane@biomatters.com> - 1.37.2-1
- Bug Fixes
  - Stops sort of user created list file.
  - Fixes bug introduced in 1.37 that removed barcodes and primers from fastq
    files instead of simply identifying samples for make.sra command.
  - Fixes bug with merge.groups initialization of the shared file.
  - Cleans up makefile.
  - Removes extra unclassified level from taxonomy files
  - Fixes make.contigs gz file error

* Fri Apr 15 2016 Shane Sturrock <shane@biomatters.com> - 1.37.1-1
- Bugfix release

* Thu Apr 07 2016 Shane Sturrock <shane@biomatters.com> - 1.37.0-1
- New Commands
  - biom.info - reads biom file and creates shared, taxonomy, constaxonomy and
    tax.summary files.
- Feature Updates
  - Adds agc and dgc methods to the cluster.split and cluster commands from the
    vsearch software package. Not available for Windows.
  - merge.groups - adds count option. Adds method and fasta parameter. Method
    options are sum, average and median. Default=sum.
  - get.groups / remove.groups - adds phylip and column options.
  - get.seqs / remove.seqs - Checks for repeat sequences names and eliminates
    them. Allows users creating their own templates to easily remove duplicate
    sequences from their reference files.
  - Remove MPI source code - MPI version is slower than non-MPI version. No
    advantage to using it.
  - unique.seqs - adds format parameter. Options are name and count.
  - Simplify makefile
  - make.file - adds numcols parameter. Options 2 or 3. Default=3, meaning
    groupName forwardFastq reverseFastq. The groupName is made from the
    beginning part of the forwardFastq file. Everything up to the first '' 
    or if no '' is found then the root of the forwardFastq filename.
  - Output number of warning and errors detected.
  - rename.seqs - adds file, map, qfile and contigsreport parameters. The map
    file allows you to revert sequence names back to original. Works with
    make.contigs to automatically rename sequences.
  - make.contigs - adds rename parameter, default=t. Renames sequences to
    reduce file sizes and greatly reduce the size of the column formatted
    distance matrix downstream. Uses the rename.seqs command to rename which
    creates a map file so you can revert to original names at any time.
  - classify.seqs - Changes cutoff parameter default to 80. This change in the
    bootstrap threshold reflects the default values in the 454 and MiSeq SOPs.
  - get.current - Adds current RAM usage and total RAM available.
  - Replaces '-' characters in sequences names with '_' characters to avoid
    downstream issues.
  - Changes default on minlength to 10 for the screen.seqs command.
  - Removed load.logfile command. Added output file to get.current and
    input/output file to set.current . These changes allow the commands to work
    together to keep track of current files between instances of mothur in a 
    more direct and easy to edit manner. You can input the output file of the
    get.current command into the set.current command using the new current
    parameter.
  - Adds includescrap parameter to the make.sra command. Default=True.
  - get.otulabels removed. Functions added to get.otus command.
  - remove.otulabels removed. Functions added to remove.otus command.
  - Adds output and printlevel parameters to classify.seqs, classify.otu,
    biom.info and summary.tax commands. Output options simple and detail.
    Default=detail.
  - Adds relabund parameter to classify.otu command.
  - Adds threshold parameter to summary.tax command.
  - Adds parent taxons to unclassified taxons for outputs of classify.seqs,
    classify.otu, biom.info commands.
  - Adds count parameter to get.sharedseqs
- Bug Fixes
  - filter.shared - modifies rareOtus label to prevent mothurConvert error.
  - make.contigs - File mismatch error with certain sequence name formats and
    multiple processors. Three column format gz file not producing group file.
  - Fixes mothurConvert error if "seed" was part of filename.
  - Removes OS limit on open files for cluster.split
  - make.sra - Fastq.info error about no inputs selected when running make.sra
    with single fastq file and oligos file.
  - cluster.split - removes limit on number of files that can be split by
    cluster.split. Limit caused "[ERROR]: Cannot open yourFasta.xxx.temp" file
    error.
  - "Illegal Instruction" error on Linux machines. Fixed in 1.29.16 release.
  - Updates Xcode project file to fix collaboration issues.
  - Fixes filter.seqs issue where sequences are not the same length by setting
    default minlength to 10 in the screen.seqs command.
  - Windows version - if files were used with less sequences than processors
    specified then empty file error.
  - Fixes make.contigs name mismatch bug and gives a slight speed boost.
  - Fixes lefse "Skipping x iter..." warning.

* Wed Jul 27 2015 Shane Sturrock <shane@biomatters.com> - 1.36.1-1
- make.file - Linux version only bug. Caused error messages about find 
  command -maxdepth parameter.
- classify.rf - Design file change caused results to be all zeros.

* Mon Jul 27 2015 Shane Sturrock <shane@biomatters.com> - 1.36.0-1
- New commands
  - set.seed - allows you to seed random.
  - make.file - creates a file containing list of fastq or gz files for 
    input to make.contigs.
- Feature updates
  - pre.cluster - added cluster method for unaligned sequences. Added align, 
    mismatch, match, gapopen, gapextend parameters.
  - set.dir - if output directory does not exist mothur will create it for you.
  - chimera.uchime - adds method tag to output files.
  - chop.seqs - adds qfile option to allows for chopping quality files.
  - classify.otu - adds threshold parameter. The threshold parameter allows 
    you to specify a cutoff for the taxonomy file that is being inputted.
  - rename.seqs - adds count, delim, and placement parameters.
  - seed parameter added to all commands to allow you to easily seed random 
    while running commands.
  - make.shared - mothur no longer checks for biom matrix type to allow for 
    more flexibility.
  - make.shared - rabund files are no longer outputted. Mothur will create a 
    rabund file with the get.rabund command.
  - set.dir - if output directory does not exist it will be created.
  - no longer create a log file simple command line option runs of mothur
  - make.sra - allow for assigning multiple sets of files to the same group 
    in 3 column format.
  - make.contigs - allow for missing reads in files.
  - metastats - remove qvalues. Also removes fortran source from mothur.
  - automatically adjust number of processors when fork() fails
  - Removes extra white spaces from mothur's print to make output files more 
    compatible with other software packages.
  - degap.seqs - adds the processors option.
  - Adds column headers to Design_File
  - phylo.diversity - adds sampledepth parameter.
  - set.dir - Sets tempdefault location to mothur's executable location to 
    help reduce "unable to find file" errors.
  - make.contigs - allow for gzipped version for fastq files as inputs.
  - Added file parameter to saved files by mothur. file=current can now be used.
- Bug fixes
  - metastats - infinite loop with certain datasets
  - cluster.split - did not allow you to use the classic option with the 
    file option.
  - make.biom - repeat labels when combining mothur OTU labels with non 
    mothur OTU labels, this can results in a duplicate "simple" label. This 
    causes an incorrect taxonomy to be assigned to the OTU.
  - remove.groups - not creating a list file for each label.
  - make.biom - remove paths from filenames to make compliant with qiime 
    parser. 
  - sffinfo - off by one in right side trimming.
  - make.contigs - Bug Fix - when using index files in version 1.35 quality 
    data was over trimmed by the length of the barcode.

* Thu Jun 04 2015 Shane Sturrock <shane@biomatters.com> - 1.35.1-1
- New commands
  - get.mimarkspackage - create blank mimarks package form for sra command 
    (see Creating a new submission)
  - make.sra - create submission ready files (see Creating a new submission)
  - Added common command line options. Can now use -q or --quiet, -h or --help,
    -v or --version.
- Feature updates
  - set.dir - added seed parameter to allow the user to set the seed for the 
    random number generator
  - make.contigs - improved speed, added pandaseq-based quality score data, 
    added kmer aligning method
  - cluster.split - allows one to use the cluster.classic option if they set 
    the classic option to T. This is likely the most ideal option for people 
    using tax level 5 or 6.
  - make.biom - added relabund file as input.
  - pcr.seqs - added fdiffs and rdiffs comments
  - cluster, cluster.split, cluster.classic, phylotype, mgcluster - Clustering 
    commands did not include the count file info. when printing list file OTU 
    order. Only effects clustering commands. *.pick commands must preserve 
    otuLabels order.
  - classify.tree - added output parameter. Output=node or taxon. Default=node. 
    Output=taxon will label tree with consensus taxonomies.
  - get.coremicrobiome - the abundance option can now accept float values. 
    abundance=1 or abundance=0.01 produce same results. Abundance=0.005 or 
    other values between 0 and 1, instead of the 1% as the lowest value.
  - chop.seqs - added keepn parameter. Default=f.
  - Restructured source files on github for easier downloads and builds.
- Bug fixes
  - cluster.split - MPI version compile issue fixed in 1.34.1.
  - summary.seqs - multiple processors Windows. fixed 1.34.2
  - summary.seqs -MPI bug fixed 1.34.2
  - pcr.seqs - use of mothur's paired primer tag instead of forward and 
    reverse tags causing improper trimming fixed in 1.34.3.
  - sffinfo - parsed sff files giving corrupt error fixed 1.34.4
  - pcr.seqs - Windows multiple processors with start and end parameters 
    giving errors fixed 1.34.4
  - make.contigs - Bug in Windows paralell processing.
  - dist.seqs - bug introduced in 1.34.4
  - rarefaction.single - returning median instead of mean.
  - make.contigs - skipping groups if invalid fastq files provided.
  - make.contigs - bug that required barcodes to process.
  - metastats - infinite loop.
  - pcr.seqs - When sequence length < primer Length + pdiffs, basic_string 
    error occurred. Rare case.
  - mothur will now read over null strings to avoid pesky sequence not found 
    errors.
  - Fixes mismatch name issue with make.contigs in v1.35.0

* Mon Jan 12 2015 Shane Sturrock <shane@biomatters.com> - 1.34.4-1
- sffinfo - parsed sff files giving corrupt error.
- pcr.seqs - Windows multiple processors with start and end parameters giving 
  errors.

* Mon Dec 15 2014 Shane Sturrock <shane@biomatters.com> - 1.34.3-1
- pcr.seqs - use of mothur's paired primer tag instead of forward and 
  reverse tags causing improper trimming.

* Thu Dec 04 2014 Shane Sturrock <shane@biomatters.com> - 1.34.2-1
- cluster.split - MPI version compile issue
- summary.seqs - multiple processors Windows

* Wed Nov 26 2014 Shane Sturrock <shane@biomatters.com> - 1.34.1-1
- Upstream update

* Wed Nov 19 2014 Shane Sturrock <shane@biomatters.com> - 1.34.0-1
- New commands
  - Classify.svm - Rank OTUs using the support vector machine learning 
    algorithm
- Feature updates
  - added shannonrange calculator to collect.single, summary.single, 
    rarefaction.single.
  - added shared parameter to count.seqs aka make.table command. Can be used 
    to transpose the shared file for use with other software packages.
  - consensus.seqs cutoff parameter can now be a float. cutoff=97.5.w
  - dist.shared - when subsample used *.ave distance matrix saved as current 
    phylip file
  - tree.shared - added Jensen-Shannon Divergence calculator, jsd and Square 
    Root Jensen-Shannon Divergence calculator, rjsd. 
    http://www.mothur.org/forum/viewtopic.php?f=5&t=2961
  - cluster.split - added the file option which allows you to enter
    your file containing your list of column and names/count files as well
    as the singleton file. This file is mothur generated, when you run
    cluster.split() with the cluster=f parameter. This can be helpful when
    you have a large dataset that you may be able to use all your
    processors for the splitting step, but have to reduce them for the
    cluster step due to RAM constraints. For example:
    cluster.split(fasta=yourFasta, taxonomy=yourTax, count=yourCount,
    taxlevel=3, cluster=f, processors=8) then cluster.split(file=yourFile,
    processors=4). This allows your to maximize your processors during the
    splitting step. Also, if you are unsure if the cluster step will have
    RAM issue with multiple processors, you can avoid running the first
    part of the command multiple times.
  - make.contigs - added checkorient parameter. 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=2993.
  - fastq.info, sffinfo, trim.flows- added checkorient parameter.
  - trim.flows can now process paired barcodes and primers.
  - fastq.info - file option can parse 3 different file formats.
  - make.shared - can now handle taxon table biom files. 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=3352
  - standard handling of mothur's oligos file across commands.
  - pcr.seqs reverse primers use pdiffs. 
    http://xn--ww-dcc.mothur.org/forum/viewtopic.php?f=4&t=3392
  - fastq.info, sffinfo, trim.flows, trim.seqs - pdiffs can be used with 
    removal of reverse primers.
  - update version of catchall to 4.0.
  - trim.seqs and make.contigs - added more output to fasta files about diffs.
  - classify.otu - added probs to unclassifieds to avoid error in make.biom 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=2835&start=10
- Bug fixes
  - fastq.info stopped processing after 100001 seqs. 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2829 fixed 1.33.1
  - make.biom picrust couldn't handle unclassifieds 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2816 fixed 1.33.1
  - create.database OutLabel bug - "cannot convert Otu0001 to an integer" 
    fixed 1.33.3
  - merge.sfffiles -Windows version caused substring error on parse. 
    fixed 1.33.2 3/11 version.
  - chimera.slayer - "[megablast] FATAL ERROR: blast: Unable to open input file
    on linux version with multiple processors. fixed 1.33.3
  - rarefaction.single - *.groups.rarefaction file labels in wrong order 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2963 fixed 1.33.3
  - align.seqs - Windows align.seqs flip=t caused segfault 
    fixed 1.33.2 3/19 version
  - summary.shared subsample issue 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2861 fixed 1.33.3
  - seq.error was changing the current fasta file to the seq file. it 
    shouldn't change the current fasta file.
  - trim.seqs - qaverage bug scrapping seqs - fixed 1.33.3 4/4.
  - make.biom - "biom error: cannot convert null to a float"
  - get.seqs, remove.seqs, remove.lineage, get.lineage, screen.seqs, pcr.seqs 
    changed read of count file causing file mismatches with count files that 
    didn't include group data.
  - clearcut - distances out of range bug
  - dist.shared - http://www.mothur.org/forum/viewtopic.php?f=3&t=3186
  - make.contigs - rindex files 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=3159&start=10#p9096
  - lefse - segfault if a sample only included 1 group.
  - cluster - nearest method caused crash.

* Mon Mar 24 2014 Shane Sturrock <shane@biomatters.com> - 1.33.3-1
- Upstream update, no details of what
* Wed Mar 05 2014 Shane Sturrock <shane@biomatters.com> - 1.33.2-1
- Remove unnecessary error messages.
* Thu Feb 26 2014 Shane Sturrock <shane@biomatters.com> - 1.33.1-1
- Fix bug in fastq.info misreporting the number of reads
* Thu Feb 20 2014 Shane Sturrock <shane@biomatters.com> - 1.33.0-1
- Feature updates
  - heatmap.bin - added otuLabels
  - make mothur "smarter" about OTULabels. OTU001 and OTU01 should be the same.
  - list.seqs, get.seqs and remove.seqs - added fastq as an option
  - add otulabels to list file
  - make.biom - added picrust and reftaxonomy parameters.
  - mothur will preserve information after sequence names in a fasta file.
  - venn - permute parameter can equal 1, 2, 3, or 4. 
  - get.oturep - changed otu numbers to be labels
  - deunique.seqs - added count table 
  - nmds - added group label to *.axes file 
  - fastq.info - added oligos, group, pdiffs, bdiffs, ldiffs, sdiffs, tdiffs 
    parameters so you can split fastq files by sample.
  - sffinfo - added group parameter so you can split sff files by group
  - dist.shared, collect.shared and summary.shared - added Jensen-Shannon 
    Divergence calculator, jsd.
  - dist.shared, collect.shared and summary.shared - added Square Root 
    Jensen-Shannon Divergence calculator, rjsd.
  - trim.seqs - added logtransform parameter to
  - trim.seqs - reorient parameter no longer requires paired barcodes and 
    primers
  - metastats, unifrac.weighted, unifrac.unweighted, parsimony, chimera.uchime,
    chimera.perseus, chimera.slayer, shhh.seqs and pre.cluster: improved work 
    balance load between processors for paralellized commands
  - get.communitytype - added dmm, pam and kmeans methods
  - get.communitytype - added calc, subsample, iters parameters for 
    calculations in pam and kmeans.
  - get.current - added directory information.
  - classify.seqs and summary.tax - added relabund parameter. relabund=t 
    outputs relative abundances to *.summary file instead of raw abundances. 
    Default=f.
- Bug fixes
  - chimera.uchime, chimera.perseus, chimera.slayer - with count table and 
    dereplicate=t caused total=0 error message.
  - sff.multiple - setting processors=1 for future commands. Not using file 
    redirects in commands it runs.
  - venn - fixed bug where command overwrote .sharedotu files when permute=t
  - pcr.seqs keepdots=f could cause an aligned template to become unaligned.
  - summary.shared - *.ave.dist matrix = 0 when processors > 2 when using the 
    subsample parameter and not using the distance parameter. 
  - classify.otu - error in *.tax.summary counts with basis=sequence when 
    using a count file. 
  - sffinfo - windows version with oligos file
  - set.current - setting processors option to 1, if not set.
  - trim.flows - printing trimmed number of flows to scrap file instead of 
    original number of flows. Caused error if you wanted to read scrapped flow 
    file.
  - get.oturep - countable caused sequence not found error.

* Thu Oct 17 2013 Shane Sturrock <shane@biomatters.com> - 1.32.1-1
- Upstream update, no details of why.

* Thu Oct 03 2013 Shane Sturrock <shane@biomatters.com> - 1.32.0-1
- Upstream update - see http://www.mothur.org/wiki/Mothur_v.1.32.0

* Thu Sep 05 2013 Shane Sturrock <shane@biomatters.com> - 1.31.2-1
- Initial build.
