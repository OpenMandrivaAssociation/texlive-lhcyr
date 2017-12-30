# revision 31795
# category Package
# catalog-ctan /macros/latex/contrib/lhcyr
# catalog-date 2012-05-22 11:10:15 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-lhcyr
Version:	20170414
Release:	1
Summary:	A non-standard Cyrillic input scheme
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lhcyr
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhcyr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhcyr.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of three LaTeX 2e styles intended for typesetting
Russian and bilingual English-Russian documents, using the lh
fonts and without the benefit of babel's language-switching
mechanisms. The packages (lhcyralt and lhcyrwin for use under
emTeX, and lhcyrkoi for use under teTeX) provide mappings
between the input encoding and the font encoding (which is
described as OT1). The way this is done does not match the way
inputenc would do the job, for output via fontenc to one of the
T2 series of font encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lhcyr/karabas.tex
%{_texmfdistdir}/tex/latex/lhcyr/kniga.tex
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/README
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/lhcyralt-hyphen.cfg
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/lhcyralt-rhyphen.tex
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/lhcyralt.sty
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/ot1lhdh.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/ot1lhfib.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/ot1lhfr.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/ot1lhr.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/ot1lhss.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/ot1lhtt.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyralt/ot1lhvtt.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/README
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/kcmf.tgz
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/lhcyrkoi-hyphen.cfg
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/lhcyrkoi-rhyphen.tex
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/lhcyrkoi.sty
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/maketfms.sh
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/ot1kcdh.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/ot1kcfib.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/ot1kcfr.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/ot1kcr.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/ot1kcss.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/ot1kctt.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/ot1kcvtt.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrkoi/special.kc
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/README
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/lhcyrwin-hyphen.cfg
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/lhcyrwin-rhyphen.tex
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/lhcyrwin.sty
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/ot1wcdh.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/ot1wcfib.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/ot1wcfr.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/ot1wcr.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/ot1wcss.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/ot1wctt.fd
%{_texmfdistdir}/tex/latex/lhcyr/lhcyrwin/ot1wcvtt.fd
%{_texmfdistdir}/tex/latex/lhcyr/otchet.tex
%{_texmfdistdir}/tex/latex/lhcyr/pismo.tex
%{_texmfdistdir}/tex/latex/lhcyr/rusfonts.tex
%{_texmfdistdir}/tex/latex/lhcyr/statya.tex
#- source
%doc %{_texmfdistdir}/source/latex/lhcyr/README
%doc %{_texmfdistdir}/source/latex/lhcyr/dvidrv.mfj
%doc %{_texmfdistdir}/source/latex/lhcyr/lhjob.mfj
%doc %{_texmfdistdir}/source/latex/lhcyr/wcjob.mfj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
