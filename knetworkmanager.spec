Summary:	knetworkmanager - KDE front end for NetworkManager
Summary(pl.UTF-8):	knetworkmanager - frontend KDE dla NetworkManagera
Name:		knetworkmanager
Version:	0.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://nouse.net/projects/KNetworkManager/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	619dbe51e58f2794c0330c58b8c4f8bd
URL:		http://en.opensuse.org/Projects/KNetworkManager
Patch0:		kde-am.patch
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
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
wyrafinowany i intuicyjny interface użytkownika który umożliwia
łatwe przełączanie między dostępnymi sieciami.

Zasięg funkcji obejmuje możliwości dostarczane przez demona
NetworkManager. Na obecną chwilę wspiera:
- Wired Ethernet Devices (IEEE 802.3)
- Wireless Ethernet Devices (IEEE 802.11): Niezaszyfrowane, WEP, WPA
  Personal, WPA Enterprise
- Virtual Private Network (VPN): OpenVPN, VPNC
- Dial-Up (PPP)

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
cp -f /usr/share/libtool/ltmain.sh admin
: > admin/libtool.m4.in
rm -f acinclude.m4
%{__make} -f admin/Makefile.common

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-distro=pld \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/dbus-1/system.d/*
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/knetworkmanager
%{_datadir}/config.kcfg/*
%{_iconsdir}/*
