%global tl_name lhcyr
%global tl_revision 77838

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A non-standard Cyrillic input scheme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lhcyr
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lhcyr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lhcyr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of three LaTeX2e styles intended for typesetting Russian
and bilingual English-Russian documents, using the lh fonts and without
the benefit of babel's language-switching mechanisms. The packages
(lhcyralt and lhcyrwin for use under emTeX, and lhcyrkoi for use under
teTeX) provide mappings between the input encoding and the font encoding
(which is described as OT1). The way this is done does not match the way
inputenc would do the job, for output via fontenc to one of the T2
series of font encodings.

