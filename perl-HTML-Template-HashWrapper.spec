#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Template-HashWrapper
Summary:	perl(HTML::Template::HashWrapper) - Easy association with HTML::Template
Name:		perl-HTML-Template-HashWrapper
Version:	1.3
Release:	0.1
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eee47d1b8e86dd309539898f6afe458d
#Patch0:		%{name}
URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
Perl module HTML::Template::HashWrapper provides a simple way to use arbitrary
hash references (and hashref‐based objects) with HTML::Template's "associate"
option.

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
%{perl_vendorlib}/HTML/Template/HashWrapper.pm
%{_mandir}/man3/*
