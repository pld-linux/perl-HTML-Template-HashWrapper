#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Template-HashWrapper
Summary:	HTML::Template::HashWrapper - Easy association with HTML::Template
Summary(pl.UTF-8):	HTML::Template::HashWrapper - łatwe połączenie z HTML::Template
Name:		perl-HTML-Template-HashWrapper
Version:	1.3
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eee47d1b8e86dd309539898f6afe458d
URL:		http://search.cpan.org/dist/HTML-Template-HashWrapper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module HTML::Template::HashWrapper provides a simple way to use
arbitrary hash references (and hashref-based objects) with
HTML::Template's "associate" option.

%description -l pl.UTF-8
Moduł Perla HTML::Template::HashWrapper udostępnia prosty sposób
używania dowolnych referencji do haszy (i obiektów opartych na
hashrefach) z opcją "associate" modułu HTML::Template.

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
