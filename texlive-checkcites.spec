Name:		texlive-checkcites
Version:	70398
Release:	1
Summary:	Check citation commands in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/checkcites
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checkcites.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checkcites.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/checkcites/checkcites.lua checkcites
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
