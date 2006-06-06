%define		_snap 060606
Summary:	knetworkmanager
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

%description -l pl
 
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

cd knetworkmanager
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
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
