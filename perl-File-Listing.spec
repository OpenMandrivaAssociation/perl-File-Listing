%define upstream_name    File-Listing
%define upstream_version 6.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Parse directory listings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-3mdv2012.0
+ Revision: 765245
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-2
+ Revision: 763759
- rebuilt for perl-5.14.x

* Tue May 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.20.0-1
+ Revision: 664980
- import perl-File-Listing

