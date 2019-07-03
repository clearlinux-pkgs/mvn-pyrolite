#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-pyrolite
Version  : 4.13
Release  : 1
URL      : https://github.com/irmen/Pyrolite/archive/pyrolite-4.13.tar.gz
Source0  : https://github.com/irmen/Pyrolite/archive/pyrolite-4.13.tar.gz
Source1  : https://repo1.maven.org/maven2/net/razorvine/pyrolite/4.13/pyrolite-4.13.jar
Source2  : https://repo1.maven.org/maven2/net/razorvine/pyrolite/4.13/pyrolite-4.13.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-pyrolite-data = %{version}-%{release}

%description
Pyrolite - Python Remote Objects "light" and Pickle for Java/.NET
Pyrolite is written by Irmen de Jong (irmen@razorvine.net).
This software is distributed under the terms written in the file `LICENSE`.

%package data
Summary: data components for the mvn-pyrolite package.
Group: Data

%description data
data components for the mvn-pyrolite package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/razorvine/pyrolite/4.13
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/razorvine/pyrolite/4.13

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/razorvine/pyrolite/4.13
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/razorvine/pyrolite/4.13


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/razorvine/pyrolite/4.13/pyrolite-4.13.jar
/usr/share/java/.m2/repository/net/razorvine/pyrolite/4.13/pyrolite-4.13.pom
