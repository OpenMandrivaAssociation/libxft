%define major 2
%define libname %mklibname xft %{major}
%define develname %mklibname -d xft

Name:		libxft
Summary:	X FreeType library
Version:	2.3.1
Release:	3
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2

BuildRequires:	pkgconfig(fontconfig) >= 2.3.93
BuildRequires:	pkgconfig(xau) >= 1.0.0
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2
BuildRequires:	x11-util-macros >= 1.0.1

%description
X FreeType library.

%package -n %{libname}
Summary:	X FreeType library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}-%{release}
Requires:	fontconfig

%description -n %{libname}
X FreeType library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}xft2-devel < 2.3.1
Obsoletes:	%{_lib}xft-static-devel < 2.3.1
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
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

%files -n %{develname}
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_mandir}/man3/Xft.*


%changelog
* Wed Jun 20 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3.1-1
+ Revision: 806534
- update to new version 2.3.1

* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.0-1
+ Revision: 783944
- version update 2.3.0

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2.0-6
+ Revision: 783366
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.2.0-5
+ Revision: 745718
- rebuild to obsolete old static pkg

* Thu Nov 24 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.2.0-4
+ Revision: 733234
- rebuild
- removed old ldconfig scriptlets
- removed defattr
- spec clean up
- disabled static build & static pkg
- removed .la files
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot
- employed major macro
- removed bad provides (xft2-devel)
- removed reqs in devel pkg

* Tue May 24 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-3
+ Revision: 678088
- rebuild

* Thu Mar 03 2011 Александр Казанцев <kazancas@mandriva.org> 2.2.0-2
+ Revision: 641427
- add lcd-cleartype for PLF

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 2.2.0-1mdv2011.0
+ Revision: 591839
- xft-config is dead
- drop merged patch 1
- new release

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.1.14-1mdv2010.1
+ Revision: 463711
- Fix spec, update patches

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1.13-3mdv2010.0
+ Revision: 425925
- rebuild

* Fri Nov 07 2008 Olivier Blin <blino@mandriva.org> 2.1.13-2mdv2009.1
+ Revision: 300407
- rebuild for new xcb

* Wed Jul 16 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 2.1.13-1mdv2009.0
+ Revision: 236612
- Update to version 2.1.13

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.1.12-5mdv2009.0
+ Revision: 223075
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 2.1.12-4mdv2008.1
+ Revision: 153315
- Update BuildRequires and rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.1.12-3mdv2008.1
+ Revision: 150855
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 30 2007 Funda Wang <fwang@mandriva.org> 2.1.12-2mdv2008.0
+ Revision: 75051
- Fix wrong rel
- introduce magiclinux's patch so that applications based on libxft could
  use embedded bitmap font too

  + Thierry Vignaud <tv@mandriva.org>
    - do not harcode man page extension


* Thu Dec 14 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.1.12-1mdv2007.0
+ Revision: 97063
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix some multiarch files
    - new upstream release (2.1.20):
      * Move XftNameUnparse to the public API
    - new upstream version (2.1.9):
      * Don't export unnecessary symbols.
    - rebuild to fix cooker uploading
    - added missing provides
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Anssi Hannula <anssi@mandriva.org>
    - mark xft-config as multiarch

  + Frederic Crozat <fcrozat@mandriva.com>
    - Move ldconfig call to correct package
    - Patch0: fix crash with rxvt-unicode
    - Patch1: enable artificial embolding

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

