Summary:	knetworkmanager - KDE front end for NetworkManager
Summary(pl.UTF-8):	knetworkmanager - frontend KDE dla NetworkManagera
Name:		knetworkmanager
Version:	0.2.2
Release:	0.svn800357.1
License:	GPL
Group:		Applications
#Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/network/%{name}-%{version}.tar.bz2
Source0:	knetworkmanager-20080424.800357.tar.bz2
# Source0-md5:	bf4a6a3360504631284e352608371f6b
URL:		http://en.opensuse.org/Projects/KNetworkManager
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-qt-devel >= 0.70
BuildRequires:	gettext-devel
BuildRequires:	hal-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdesdk-kapptemplate >= 3:3.2.0
BuildRequires:	libiw-devel
BuildRequires:	libnl-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	NetworkManager >= 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNetworkManager is the KDE front end for NetworkManager. It provides a
sophisticated and intuitive user interface which enables users easily
to switch their network environment.

The range of functions encompasses the features implemented by
NetworkManager daemon. Up until now NetworkManager supports:
- Wired Ethernet Devices (IEEE 802.3)
- Wireless Ethernet Devices (IEEE 802.11): Unencrypted, WEP, WPA
  Personal, WPA Enterprise
- Virtual Private Network (VPN): OpenVPN, VPNC
- Dial-Up (PPP)

%description -l pl.UTF-8
KnetworkManager to frontend KDE dla NetworkManagera. Dostarcza
wyrafinowany i intuicyjny interface użytkownika który umożliwia łatwe
przełączanie między dostępnymi sieciami.

Zasięg funkcji obejmuje możliwości dostarczane przez demona
NetworkManager. Na obecną chwilę wspiera:
- Wired Ethernet Devices (IEEE 802.3)
- Wireless Ethernet Devices (IEEE 802.11): Niezaszyfrowane, WEP, WPA
  Personal, WPA Enterprise
- Virtual Private Network (VPN): OpenVPN, VPNC
- Dial-Up (PPP)

%prep
%setup -q -n %{name}

%build
%{__make} -f Makefile.cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
	--with-distro=pld
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

# no -devel
rm -f $RPM_BUILD_ROOT%{_includedir}/*.h

# no .la loader
rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/knetworkmanager.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libkdeinit_knetworkmanager.la

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knetworkmanager
/etc/dbus-1/system.d/knetworkmanager.conf
%attr(755,root,root) %{_libdir}/libkdeinit_knetworkmanager.so
%attr(755,root,root) %{_libdir}/kde3/knetworkmanager.so
%{_datadir}/apps/knetworkmanager
%{_datadir}/config.kcfg/knetworkmanager.kcfg
%{_datadir}/autostart/knetworkmanager.desktop
%{_datadir}/servicetypes/knetworkmanager_plugin.desktop
%{_datadir}/servicetypes/knetworkmanager_vpnplugin.desktop
%{_desktopdir}/kde/knetworkmanager.desktop
%{_iconsdir}/crystalsvg/*/apps/knetworkmanager.png
