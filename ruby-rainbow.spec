#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname rainbow
Summary:	Ruby String class extension enabling coloring text on ANSI terminals
Name:		ruby-%{pkgname}
Version:	3.0.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	a4959de1d41c77d25eb56dbeeb37cf39
URL:		https://github.com/sickill/rainbow
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.3
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rainbow is an extension to the Ruby String class adding support for
colorizing text on ANSI terminals.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
rspec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown Changelog.md LICENSE
%{ruby_vendorlibdir}/rainbow.rb
%{ruby_vendorlibdir}/rainbow
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
