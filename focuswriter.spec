%define debug_package %{nil}

Name:		focuswriter
Version:	1.8.2
Release:	1
Summary:	A full-screen, distraction-free writing program

Group:		Editors
License:	GPLv3+
URL:		http://gottcode.org/%{name}/
Source:		http://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2

BuildRequires:	libzip-devel
BuildRequires:  qt5-devel
BuildRequires:	hunspell-devel
BuildRequires:	enchant-devel
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(zlib)

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
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/metainfo/*
%{_mandir}/man1/%{name}.*
