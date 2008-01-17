Name: xset
Version: 1.0.3
Release: %mkrel 2
Summary: User preference utility for X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libxfontcache-devel	>= 1.0.4
BuildRequires: libxxf86misc-devel	>= 1.0.1
BuildRequires: libxmu-devel		>= 1.0.0

%description
The xset program is used to set various user preference options of the display.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xset
%{_mandir}/man1/xset.*
