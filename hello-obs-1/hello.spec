Name:		hello-obs
Version:	1
Release:	1%{?dist}
Summary:	A test package for OBS

Group:		Test
License:	GPLv3
URL:		https://github.com/UHaider/hello-obs.git
Source0:	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%description
This is just for OBS testing.

%prep
%setup -q


%build
make 

%install
make install DESTDIR=%{buildroot}


%files
%defattr(4755,root,root,0755)
/usr/bin/helloobs
