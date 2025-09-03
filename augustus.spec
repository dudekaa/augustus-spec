%define packagePatch 1
%global debug_package %{nil}

Name:    augustus 
Version: 4.0.0
Release: %{packagePatch}%{?dist}
Summary: Augustus is a fork of the Julius project that intends to incorporate gameplay changes.

Group:   Games
License: AGPLv3
URL:     https://github.com/Keriew/augustus
Source:  https://github.com/Keriew/augustus/archive/refs/tags/v%{version}.tar.gz
Source1: https://github.com/dudekaa/augustus-spec/archive/refs/tags/v%{version}-%{packagePatch}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: SDL2-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: libpng-devel
BuildRequires: desktop-file-utils
Requires: SDL2
Requires: SDL2_mixer
Requires: libpng 

%description
The aim of this project is to provide enhanced, customizable gameplay to Caesar 3 using project Julius UI enhancements.

Augustus is able to load Caesar 3 and Julius saves, however saves made with Augustus will not work outside Augustus.

Gameplay enhancements include:

  * Roadblocks
  * Market special orders
  * Global labour pool
  * Partial warehouse storage
  * Increased game limits
  * Zoom controls
  * And more!


%prep
%setup
%setup -T -D -a 1


%build
#configure
mkdir build && cd build
%cmake -DIS_RELEASE_VERSION=1 ..
%cmake_build
%ctest


%install
install -pDm0755 %_builddir/%{name}-%{version}/build/redhat-linux-build/%{name} %{buildroot}%{_bindir}/%{name}

# menu item
install -pDm0644 %_builddir/%{name}-%{version}/%{name}-spec-%{version}-%{packagePatch}/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop


%files
/usr/bin/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Sep 03 2025 Arnošt Dudek <arnost@arnostdudek.cz> - 1.8.0-1
- Initial build
