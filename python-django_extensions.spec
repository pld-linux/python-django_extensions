%define		module		django-extensions
Summary:	Django Custom Management Command Extensions
Name:		python-django_extensions
Version:	0.7.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	c82b38a1f82fb4724565ad1bb61652d0
URL:		http://django-command-extensions.googlecode.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
Requires:	python-django >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Django Custom Management Command Extensions

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/django_extensions
%{py_sitescriptdir}/django_extensions-*.egg-info
