%define upstream_name    Dist-Zilla-Plugin-GitFmtChanges
Name:		perl-%{upstream_name}
Version:	0.006
Release:	1

Summary:	This Dist::Zilla plugin writes a CHANGES file with commits
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Text::Wrap)
BuildArch:	noarch

%description
This Dist::Zilla plugin writes a CHANGES file that contains formatted
commit information from recent git logs. The CHANGES file is formatted
using the "--format" option of the git log command. This makes it easy to
make the CHANGES file look the way you want it to.

This is based on Dist::Zilla::Plugin::ChangelogFromGit.

This plugin has the following configuration variables:

%prep
%setup -q -n Dist-Zilla-Plugin-GitFmtChanges-0.006

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml LICENSE Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

