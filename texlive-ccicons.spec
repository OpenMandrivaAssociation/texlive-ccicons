Name:		texlive-ccicons
Version:	1.3
Release:	1
Summary:	LaTeX support for Creative Commons icons
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ccicons
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the means to typeset Creative Commons
icons, in documents licensed under CC licences. A font (in
Adobe Type 1 format) and LaTeX support macros are provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/ccicons/ccicons-u.enc
%{_texmfdistdir}/fonts/map/dvips/ccicons/ccicons.map
%{_texmfdistdir}/fonts/tfm/public/ccicons/ccicons.tfm
%{_texmfdistdir}/fonts/type1/public/ccicons/ccicons.pfb
%{_texmfdistdir}/tex/latex/ccicons/ccicons.sty
%doc %{_texmfdistdir}/doc/latex/ccicons/ccicons.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ccicons/ccicons.dtx
%doc %{_texmfdistdir}/source/latex/ccicons/ccicons.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
