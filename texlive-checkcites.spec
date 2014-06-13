# revision 28572
# category Package
# catalog-ctan /support/checkcites
# catalog-date 2012-12-18 18:32:41 +0100
# catalog-license lppl1.3
# catalog-version 1.0i
Name:		texlive-checkcites
Version:	1.0i
Release:	6
Summary:	Check citation commands in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/checkcites
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checkcites.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checkcites.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-checkcites.bin = %{EVRD}

%description
The package provides a lua script written for the sole purpose
of detecting undefined and unused references from LaTeX
auxiliary or bibliography files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/checkcites
%{_texmfdistdir}/scripts/checkcites/checkcites.lua
%doc %{_texmfdistdir}/doc/support/checkcites/README
%doc %{_texmfdistdir}/doc/support/checkcites/checkcites-doc.pdf
%doc %{_texmfdistdir}/doc/support/checkcites/checkcites-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/checkcites/checkcites.lua checkcites
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
