Name: xset
Version: 1.2.3
Release: 7
Summary: User preference utility for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xset program is used to set various user preference options of the display.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

#

%files
%{_bindir}/xset
%{_mandir}/man1/xset.*


%changelog
* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-1mdv2012.0
+ Revision: 699273
- update to new version 1.2.2

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2
+ Revision: 671363
- mass rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Sun Aug 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 567610
- update to new version 1.2.0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2010.1
+ Revision: 524465
- rebuilt for 2010.1

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 448654
- new release

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.4-3mdv2009.1
+ Revision: 350780
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-2mdv2009.0
+ Revision: 266154
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 193002
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 154303
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 72610
- fix man page extension
- new release


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:24:58 (31400)
- fill in a couple of missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

