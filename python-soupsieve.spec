# TODO: doc (requires mkdocs-material)
#
# Conditional build:
%bcond_with	doc	# API documentation
%bcond_without	tests	# unit tests

Summary:	Modern CSS selector implementation for Beautiful Soup
Summary(pl.UTF-8):	Współczesna implementacja wybierania CSS dla Beautiful Soup
Name:		python-soupsieve
# keep 1.x here for python2 support
Version:	1.9.6
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/soupsieve/
Source0:	https://files.pythonhosted.org/packages/source/s/soupsieve/soupsieve-%{version}.tar.gz
# Source0-md5:	056fc893f7e6d4df64c136e07c426342
URL:		https://pypi.org/project/soupsieve/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-backports.functools_lru_cache
BuildRequires:	python-bs4 >= 4.9
BuildRequires:	python-html5lib
BuildRequires:	python-lxml
BuildRequires:	python-pytest
%endif
%if %{with doc}
BuildRequires:	python-backports.functools_lru_cache
BuildRequires:	python-mkdocs-material >= 2.2.5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Soup Sieve is a CSS selector library designed to be used with
Beautiful Soup 4 (bs4). It aims to provide selecting, matching, and
filtering using modern CSS selectors. Soup Sieve currently provides
selectors from the CSS level 1 specifications up through the latest
CSS level 4 drafts and beyond (though some are not yet implemented).

%description -l pl.UTF-8
Soup Sieve to biblioteka wybierania CSS zaprojektowana z myślą o
używaniu w Beautiful Soup 4 (bs4). Celem jest zapewnienie wyboru,
dopasowywania i filtrowania przy użyciu współczesnego wybierania CSS.
Soup Sieve obecnie zawiera wybieranie ze specyfikacji od CSS poziomu 1
do najnowszych szkiców CSS poziomu 4 i nowszych (ale nie wszystkie są
zaimplementowane).

%package apidocs
Summary:	API documentation for Python soupsieve module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona soupsieve
Group:		Documentation

%description apidocs
API documentation for Python soupsieve module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona soupsieve.

%prep
%setup -q -n soupsieve-%{version}

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif

%if %{with doc}
mkdocs build --clean --verbose --strict
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py_sitescriptdir}/soupsieve
%{py_sitescriptdir}/soupsieve-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
