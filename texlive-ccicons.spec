Name:		texlive-ccicons
Epoch:		1
Version:	54512
Release:	2
Summary:	LaTeX support for Creative Commons icons
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ccicons
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
