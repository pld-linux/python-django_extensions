%define		module		django-extensions
Summary:	Django Custom Management Command Extensions
Name:		python-django_extensions
Version:	0.4.1
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://django-command-extensions.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	39e38bee61538f50b6d3a322624b0f22
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
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/django_extensions
%{py_sitescriptdir}/django_extensions-*.egg-info
