%define major 2
%define libname %mklibname xft %{major}
%define develname %mklibname -d xft
%define build_plf 0

%if %build_plf
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%endif

Name: libxft
Summary:  X FreeType library
Version: 2.2.0
Release: 5%{?extrarelsuffix}
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2
# (fwang) Patch from MagicLinux, enable embedded bitmap option in Xft
# (pzanoni): disabled as the 2.1.14 release seems to integrate part of it in a
# different way
#Patch1: libXft-2.1.8-add-embeddedbitmap-and-gamma-option.patch
%if %build_plf
Patch2:	libXft-2.1.14-lcd-cleartype.patch
%endif

BuildRequires: pkgconfig(fontconfig) >= 2.3.93
BuildRequires: pkgconfig(xau) >= 1.0.0
BuildRequires: pkgconfig(xrender) >= 0.9.0.2
BuildRequires: x11-util-macros >= 1.0.1

%description
X FreeType library

%package -n %{libname}
Summary:  X FreeType library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
X FreeType library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xft2-devel
Obsoletes: %{_lib}xft-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXft-%{version}
%if %build_plf
%patch2 -p1
%endif

%build
%configure2_5x	\
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libXft.so.%{major}*

%files -n %{develname}
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_mandir}/man3/Xft.*
