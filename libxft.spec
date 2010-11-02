%define libxft %mklibname xft 2
%define develname %mklibname -d xft
%define staticdevelname %mklibname -d -s xft

Name: libxft
Summary:  X FreeType library
Version: 2.2.0
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2
# (fwang) Patch from MagicLinux, enable embedded bitmap option in Xft
# (pzanoni): disabled as the 2.1.14 release seems to integrate part of it in a
# different way
#Patch1: libXft-2.1.8-add-embeddedbitmap-and-gamma-option.patch
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libfontconfig-devel >= 2.3.93
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-util-macros >= 1.0.1

%description
X FreeType library

#-----------------------------------------------------------

%package -n %{libxft}
Summary:  X FreeType library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxft}
X FreeType library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxft} = %{version}
Requires: freetype2-devel >= 2.1.10
Provides: xft2-devel = %{version}-%{release}
Provides: libxft-devel = %{version}-%{release}
Obsoletes: %libxft-devel

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXft.so
%{_libdir}/libXft.la
%{_libdir}/pkgconfig/xft.pc
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_mandir}/man3/Xft.*

#-----------------------------------------------------------

%package -n %{staticdevelname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: xft2-static-devel = %{version}-%{release}
Provides: libxft-static-devel = %{version}-%{release}
Obsoletes: %{libxft}-static-devel

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticdevelname}
Static development files for %{name}

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/libXft.a

#-----------------------------------------------------------

%prep
%setup -q -n libXft-%{version}
#%patch1 -p0 -b .embeddedbitmap

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libxft} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libxft} -p /sbin/ldconfig
%endif

%files -n %{libxft}
%defattr(-,root,root)
%{_libdir}/libXft.so.2
%{_libdir}/libXft.so.%{version}
