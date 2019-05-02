Name:		texlive-hyphen-lithuanian
Version:	20190406
Release:	1
Summary:	Lithuanian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-lithuanian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Lithuanian in L7X and UTF-8 encodings.
\lefthyphenmin and \righthyphenmin have to be at least 2.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-lithuanian
%_texmf_language_def_d/hyphen-lithuanian
%_texmf_language_lua_d/hyphen-lithuanian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-lithuanian <<EOF
\%% from hyphen-lithuanian:
lithuanian loadhyph-lt.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-lithuanian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-lithuanian <<EOF
\%% from hyphen-lithuanian:
\addlanguage{lithuanian}{loadhyph-lt.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-lithuanian
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-lithuanian <<EOF
-- from hyphen-lithuanian:
	['lithuanian'] = {
		loader = 'loadhyph-lt.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-lt.pat.txt',
		hyphenation = '',
	},
EOF
