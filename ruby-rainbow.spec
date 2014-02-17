#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname rainbow
Summary:	Ruby String class extension enabling coloring text on ANSI terminals
Name:		ruby-%{pkgname}
Version:	1.1.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	c5bb469c89b151668f8e4eeb37e98cbf
URL:		http://ku1ik.com/
BuildRequires:	ruby
BuildRequires:	rubygem(minitest)
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rainbow is an extension to the Ruby String class adding support for
colorizing text on ANSI terminals.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%if %{with tests}
# Force coloring, otherwise it won't color
CLICOLOR_FORCE=1 ruby test/*_test.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown Changelog LICENSE
%{ruby_vendorlibdir}/rainbow.rb
%{ruby_vendorlibdir}/ansi_color.rb
%{ruby_vendorlibdir}/ansi_rgb.rb
