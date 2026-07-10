%global tl_name checkcites
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.8
Release:	%{tl_revision}.1
Summary:	Check citation commands in a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/checkcites
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/checkcites.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/checkcites.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(checkcites.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a lua script written for the sole purpose of
detecting undefined and unused references from LaTeX auxiliary or
bibliography files.

