%define upstream_name    Dist-Zilla-Plugin-GitFmtChanges
%define upstream_version 0.003

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Text::Wrap)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This Dist::Zilla plugin writes a CHANGES file that contains formatted
commit information from recent git logs. The CHANGES file is formatted
using the "--format" option of the git log command. This makes it easy to
make the CHANGES file look the way you want it to.

This is based on Dist::Zilla::Plugin::ChangelogFromGit.

This plugin has the following configuration variables:

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
%doc META.yml LICENSE Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


