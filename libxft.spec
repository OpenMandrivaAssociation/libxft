# libxft is used by pango, pango is used by gst-plugins-base,
# gst-plugins-base is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 2
%define libname %mklibname xft %{major}
%define devname %mklibname xft -d
%define lib32name %mklib32name xft %{major}
%define dev32name %mklib32name xft -d

Summary:	X FreeType library
Name:		libxft
Version:	2.3.7
Release:	2
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.xz
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xrender)
%if %{with compat32}
BuildRequires:	devel(libfontconfig)
BuildRequires:	devel(libfreetype)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXrender)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXdmcp)
BuildRequires:	devel(libz)
BuildRequires:	devel(libbz2)
BuildRequires:	devel(libpng16)
BuildRequires:	devel(libuuid)
BuildRequires:	devel(libexpat)
%endif

%description
X FreeType library.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	X FreeType library
Group:		Development/X11
Provides:	%{name} = %{EVRD}
Requires:	fontconfig

%description -n %{libname}
X FreeType library.

%files -n %{libname}
%{_libdir}/libXft.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%doc %{_mandir}/man3/Xft*.*

#----------------------------------------------------------------------------

%if %{with compat32}
%package -n %{lib32name}
Summary:	X FreeType library (32-bit)
Group:		Development/X11
Provides:	%{name} = %{EVRD}
Requires:	fontconfig

%description -n %{lib32name}
X FreeType library.

%files -n %{lib32name}
%{_prefix}/lib/libXft.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
Development files for %{name}.

%files -n %{dev32name}
%{_prefix}/lib/libXft.so
%{_prefix}/lib/pkgconfig/xft.pc
%endif

%prep
%autosetup -n libXft-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
