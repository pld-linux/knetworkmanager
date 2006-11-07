%define		_snap 060606
Summary:	knetworkmanager - KDE front end for NetworkManager
Summary(pl):	knetworkmanager - frontend KDE dla NetworkManagera
Name:		knetworkmanager
Version:	0
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	202a19f02bfd38cf2a693ee9258dfe5e
URL:		http://en.opensuse.org/Projects/KNetworkManager
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040805
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

%description -l pl
KnetworkManager to frontend KDE dla NetworkManagera. Dostarcza
wyrafinowany i intuicyjny interface u¿ytkownika który umo¿liwia ³atwe
prze³±czanie miêdzy dostêpnymi sieciami.

Zasiêg funkcji obejmuje mo¿liwo¶ci dostarczane przez demona
NetworkManager. Na obecn± chwilê wspiera:
- Wired Ethernet Devices (IEEE 802.3)
- Wireless Ethernet Devices (IEEE 802.11): Niezaszyfrowane, WEP, WPA
  Personal, WPA Enterprise
- Virtual Private Network (VPN): OpenVPN, VPNC
- Dial-Up (PPP)

%prep
%setup -q -n %{name}

%build
cp -f /usr/share/automake/config.sub admin
#export PATH=/usr/share/unsermake:$PATH
%{__make} -f admin/Makefile.common cvs

export CXXFLAGS="$CXXFLAGS -DDBUS_API_SUBJECT_TO_CHANGE"
export CPPFLAGS="$CPPFLAGS -DDBUS_API_SUBJECT_TO_CHANGE"
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir} \
	--with-extra-includes=%{_includedir}/dbus-1.0:%{_libdir}/dbus-1.0/include

%{__make} -C knetworkmanager

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
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
