#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Package
%define		pnam	Variant
%include	/usr/lib/rpm/macros.perl
Summary:	Package::Variant - Parameterizable packages
#Summary(pl.UTF-8):	
Name:		perl-Package-Variant
Version:	1.002000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Package/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fc0b756835c26d6d6dca711021fb94c0
URL:		http://search.cpan.org/dist/Package-Variant/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Import-Into >= 1
BuildRequires:	perl-Module-Runtime >= 0.013
BuildRequires:	perl-strictures >= 1
BuildRequires:	perl-Test-Fatal
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to build packages that return different
variations depending on what parameters are given.

Users of your package will receive a subroutine able to take
parameters and return the name of a suitable variant package.
The implementation does not care about what kind of package it builds.

There are two important parts to creating a variable package. You
first have to give Package::Variant some basic information about what
kind of package you want to provide, and how. The second part is
implementing a method receiving the user's arguments and generating
your variants.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Package/Variant.pm
%{_mandir}/man3/*
