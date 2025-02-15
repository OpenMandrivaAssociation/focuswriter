%define debug_package %{nil}

Name:		focuswriter
Version:	1.8.10
Release:	1
Summary:	A full-screen, distraction-free writing program
Group:		Editors
License:	GPLv3+
URL:		https://gottcode.org/%{name}/
Source:		https://gottcode.org/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:	cmake(qt6)
BuildRequires:	qmake-qt6
BuildRequires:  Gettext
BuildRequires:	libzip-devel
#BuildRequires:  qt5-devel
BuildRequires:	hunspell-devel
BuildRequires:	enchant-devel
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:  cmake(VulkanHeaders)
BuildRequires:	qt6-qttools
BuildRequires:	pkgconfig(zlib)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(hunspell)

%description
A full-screen, distraction-free writing program. 
You can customize your environment by changing the font, colors, and
background image to add ambiance as you type. FocusWriter features
an on-the-fly updating word count, optional auto-save, optional daily
goals, and an interface that hides away to allow you to focus more 
clearly; additionally, when you open the program your current 
work-in-progress will automatically load and position you at the end
of your document, so that you can immediately jump back in.

%prep
%setup -q
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
#{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/metainfo/*
%{_mandir}/man1/%{name}.*
