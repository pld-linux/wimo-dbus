Summary:	WiMo-DBus
Summary(pl.UTF-8):	WiMo-DBus
Name:		wimo-dbus
Version:	0.6.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/wimo/%{name}-%{version}.tar.bz2
# Source0-md5:	d8c638061395a32d39ead23fe8259dfe
URL:		http://www.wimol.org/
BuildRequires:	nant
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Windows Mobile devices support for Linux desktop.
WiMo-DBus provides WiMo DBus interfaces.

%prep
%setup -q

%build
nant -D:PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
nant install \
	-D:DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
/etc/dbus-1/system.d/org.wimo.dccm.conf
%{_libdir}/mono/gac/%{name}
%{_libdir}/mono/%{name}
%{_pkgconfigdir}/%{name}.pc
