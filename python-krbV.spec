#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-krbV
Version  : 1.0.90
Release  : 15
URL      : http://pypi.debian.net/python-krbV/python-krbV-1.0.90.tar.bz2
Source0  : http://pypi.debian.net/python-krbV/python-krbV-1.0.90.tar.bz2
Summary  : Python extension module for Kerberos 5
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: python-krbV-license
Requires: python-krbV-python
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : e2fsprogs-dev
BuildRequires : krb5-dev
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools-legacypython

%description
python-krbV allows python programs to use Kerberos 5 authentication and security.

%package legacypython
Summary: legacypython components for the python-krbV package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the python-krbV package.


%package license
Summary: license components for the python-krbV package.
Group: Default

%description license
license components for the python-krbV package.


%package python
Summary: python components for the python-krbV package.
Group: Default
Provides: python-krbv-python

%description python
python components for the python-krbV package.


%prep
%setup -q -n python-krbV-1.0.90

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535067915
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-krbV
cp COPYING %{buildroot}/usr/share/doc/python-krbV/COPYING
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/example/krbV-code-snippets.py
/usr/test/python-krbV-test.py

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/python-krbV/COPYING

%files python
%defattr(-,root,root,-)
