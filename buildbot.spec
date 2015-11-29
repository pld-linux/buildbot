Summary:	BuildBot build automation system
Name:		buildbot
Version:	0.8.1
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://dl.sourceforge.net/buildbot/%{name}-%{version}.tar.gz
# Source0-md5:	53b7defb3f8919413907990269b7566d
URL:		http://www.buildbot.net/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Requires:	python-TwistedConch
Requires:	python-TwistedCore
Requires:	python-TwistedMail
Requires:	python-TwistedWeb
Requires:	python-TwistedWords
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BuildBot is a system to automate the compile/test cycle required
by most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure. The guilty developer can be identified
and harassed without human intervention. By running the builds on a
variety of platforms, developers who do not have the facilities to
test their changes everywhere before checkin will at least know
shortly afterwards whether they have broken the build or not. Warning
counts, lint checks, image size, compile time, and other build
parameters can be tracked over time, are more visible, and are
therefore easier to improve.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README UPGRADING
%doc contrib
%attr(755,root,root) %{_bindir}/buildbot
%{py_sitescriptdir}/buildbot
%{py_sitescriptdir}/buildbot*.egg-info
