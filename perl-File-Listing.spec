%define modname	File-Listing
%define modver	6.02

Summary:	Parse directory listings
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl-devel

%description
This module exports a single function called parse_dir(), which can be used
to parse directory listings.

The first parameter to parse_dir() is the directory listing to parse. It
can be a scalar, a reference to an array of directory lines or a glob
representing a filehandle to read the directory listing from.

The second parameter is the time zone to use when parsing time stamps in
the listing. If this value is undefined, then the local time zone is
assumed.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*

