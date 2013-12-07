%define major 2
%define libname %mklibname xft %{major}
%define devname %mklibname -d xft

Summary:	X FreeType library
Name:		libxft
Version:	2.3.1
Release:	6
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2
BuildRequires:	pkgconfig(fontconfig) >= 2.3.93
BuildRequires:	pkgconfig(xau) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2

%description
X FreeType library.

%package -n %{libname}
Summary:	X FreeType library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}
Requires:	fontconfig

%description -n %{libname}
X FreeType library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXft-%{version}

%build
%configure2_5x	\
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXft.so.%{major}*

%files -n %{devname}
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_mandir}/man3/Xft.*

