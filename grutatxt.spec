%define oname	Grutatxt

Name:           grutatxt
Summary:        Text to HTML converter
Version:        2.0.16
Release:	1
Source0:        http://triptico.com/download/%{oname}-%{version}.tar.gz
URL:            http://www.triptico.com/software/grutatxt.html
Group:          Text tools
License:        GPLv2
BuildArch:	noarch
Provides:	%{oname} = %{EVRD}

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
install -p -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1

%files 
%doc AUTHORS Changelog.1 README RELEASE_NOTES TODO
%doc doc/grutatxt_apache_handlers.txt doc/grutatxt_markup.txt
%{_bindir}/%{name}
%{_bindir}/pod2%{name}
%{perl_vendorlib}/%{oname}.pm
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
