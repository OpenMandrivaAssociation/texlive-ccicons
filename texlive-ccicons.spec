# revision 30020
# category Package
# catalog-ctan /fonts/ccicons
# catalog-date 2013-04-17 11:42:52 +0200
# catalog-license lppl1.3
# catalog-version 1.5
Name:		texlive-ccicons
Epoch:		1
Version:	1.5
Release:	9
Summary:	LaTeX support for Creative Commons icons
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ccicons
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to typeset Creative Commons
icons, in documents licensed under CC licences. A font (in
Adobe Type 1 format) and LaTeX support macros are provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/ccicons/ccicons-u.enc
%{_texmfdistdir}/fonts/map/dvips/ccicons/ccicons.map
%{_texmfdistdir}/fonts/opentype/public/ccicons/ccicons.otf
%{_texmfdistdir}/fonts/tfm/public/ccicons/ccicons.tfm
%{_texmfdistdir}/fonts/type1/public/ccicons/ccicons.pfb
%{_texmfdistdir}/tex/latex/ccicons/ccicons.sty
%doc %{_texmfdistdir}/doc/fonts/ccicons/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/ccicons/OFL.txt
%doc %{_texmfdistdir}/doc/latex/ccicons/ccicons.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/ccicons/ccicons.sfd
%doc %{_texmfdistdir}/source/latex/ccicons/ccicons.dtx
%doc %{_texmfdistdir}/source/latex/ccicons/ccicons.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
