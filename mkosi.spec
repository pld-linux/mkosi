#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	Build Bespoke OS Images
Name:		mkosi
Version:	20.2
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f55ced5f4d136f779ab54eb29240210a
URL:		https://github.com/systemd/mkosi
#BuildRequires:	-
#Requires:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

echo "import setuptools; setuptools.setup()" >setup.py

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.md README.md docs
%attr(755,root,root) %{_bindir}/%{name}
%{py3_sitescriptdir}/mkosi
%{py3_sitescriptdir}/mkosi-%{version}-py*.egg-info
