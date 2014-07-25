Name:		focuswriter
Version:	1.4.4
Release:	2
Summary:	A full-screen, distraction-free writing program

Group:		Editors
License:	GPLv3+
URL:		http://gottcode.org/%{name}/
Source:		http://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2

BuildRequires:	pkgconfig(libzip)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(hunspell)

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

%build
%qmake_qt4 PREFIX=%{_prefix}
%make

%install
make install INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm

%changelog

