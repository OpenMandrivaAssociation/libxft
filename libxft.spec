%define major 2
%define libname %mklibname xft %{major}
%define devname %mklibname xft -d

Summary:	X FreeType library
Name:		libxft
Version:	2.3.3
Release:	1
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xrender)

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
%{_mandir}/man3/Xft.*

#----------------------------------------------------------------------------

%prep
%autosetup -n libXft-%{version} -p1

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install
