%define oname	Grutatxt

Name:           grutatxt
Summary:        Text to HTML converter
Version:        2.0.16
Release:	%mkrel 1
Source0:        http://triptico.com/download/%{oname}-%{version}.tar.gz
URL:            http://www.triptico.com/software/grutatxt.html
Group:          Text tools
License:        GPLv2
BuildArch:	noarch
Provides:	%{oname} = %{EVRD}

Requires:       perl


%description
Grutatxt is a plain text to HTML (and other formats) converter.
It successfully converts subtle text markup to lists, bold, italics, 
tables and headings to their corresponding HTML, troff, man page or 
LaTeX markup without having to write unreadable source text files. 
Grutatxt is a Perl module and a command line utility, 
and is the main text renderer in the Gruta CMS.


%prep 
%setup -q -n %{oname}-%{version}

%build 
perl Makefile.PL DESTDIR=%{buildroot} INSTALL_BASE=/usr SITEPREFIX=/usr INSTALLSITEMAN1DIR=%{_mandir}/man1 INSTALLSITEMAN3DIR=%{_mandir}/man3 INSTALLSITELIB=%{_libdir}/perl5/5.12.3
%make

%install
%makeinstall
mkdir -p %{buildroot}/%{_mandir}/man1/
install -p -m 0644 %{name}.1* %{buildroot}/%{_mandir}/man1/

%files 
%doc AUTHORS Changelog.1 README RELEASE_NOTES TODO doc/grutatxt_apache_handlers.txt doc/grutatxt_markup.txt
%{_bindir}/%{name}
%{_bindir}/pod2%{name}
%{_libdir}/perl5/*/%{oname}.pm
%{_libdir}/perl5/i386-linux-thread-multi/perllocal.pod
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
