%define upstream_name    File-Listing
%define upstream_version 6.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Parse directory listings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTTP::Date)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


