# TODO: Fix tests
#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	django_extensions
Summary:	Django Custom Management Command Extensions
Summary(pl.UTF-8):	Rozszerzenie komend zarządzających Django
Name:		python-%{module}
Version:	1.9.0
Release:	10
License:	MIT
Group:		Libraries/Python
#Source0:	https://pypi.python.org/packages/7f/da/1245fe47d1a2ca8d2d03b3cdbc886e64c94a8c2d3b6f99e3464d507a7c29/django-extensions-%{version}.tar.gz
Source0:	https://github.com/django-extensions/django-extensions/archive/%{version}.tar.gz
# Source0-md5:	bbb01383b6f199dfd1a6a64a3cc415e3
URL:		https://github.com/django-extensions/django-extensions
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-shortuuid
BuildRequires:	python-six >= 1.2
BuildRequires:	python-tox
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-shortuuid
BuildRequires:	python3-six >= 1.2
BuildRequires:	python3-tox
%endif
Requires:	python-django
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Django Extensions is a collection of custom extensions for the Django
Framework.

%description -l pl.UTF-8
Zbiór rozszerzeń dla Django.

%package -n python3-%{module}
Summary:	Django Custom Management Command Extensions
Summary(pl.UTF-8):	Rozszerzenie komend zarządzających Django
Group:		Libraries/Python
Requires:	python3-django
Requires:	python3-modules

%description -n python3-%{module}
Django Extensions is a collection of custom extensions for the Django
Framework.

%description -n python3-%{module} -l pl.UTF-8
Zbiór rozszerzeń dla Django.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n django-extensions-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
