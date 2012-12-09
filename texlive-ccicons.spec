# revision 26608
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-ccicons
Version:	20120807
Release:	1
Summary:	TeXLive ccicons package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccicons.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive ccicons package.

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
%{_texmfdistdir}/fonts/tfm/public/ccicons/ccicons.tfm
%{_texmfdistdir}/fonts/type1/public/ccicons/ccicons.pfb
%{_texmfdistdir}/tex/latex/ccicons/ccicons.sty
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120807-1
+ Revision: 812095
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 750042
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718019
- texlive-ccicons
- texlive-ccicons
- texlive-ccicons
- texlive-ccicons
- texlive-ccicons

