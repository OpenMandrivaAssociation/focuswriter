Name:		focuswriter
Version:	1.4.1
Release:	%mkrel 2
Summary:	A full-screen, distraction-free writing program

Group:		Office/Word processor
License:	GPLv3+
URL:		http://gottcode.org/%{name}/
Source:		http://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2

BuildRequires:	libzip-devel
BuildRequires:	qt4-devel >= 4.6
BuildRequires:	hunspell-devel
BuildRequires:	enchant-devel

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
%setup -q -n %{name}-%{version}

%build
%qmake_qt4 PREFIX=%{_prefix}
%make %{?_smp_mflags}

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm


%changelog

* Fri Jan 11 2013 umeabot <umeabot> 1.4.1-2.mga3
+ Revision: 350615
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Thu Jan 03 2013 vaci0 <vaci0> 1.4.1-1.mga3
+ Revision: 338332
- Updated to version 1.4.1

* Mon Oct 22 2012 dams <dams> 1.4.0-1.mga3
+ Revision: 309258
- udpate %%group
- new version 1.4.0

* Sat Sep 08 2012 vaci0 <vaci0> 1.3.90-1.mga3
+ Revision: 289690
- Updated to version 1.3.90

* Wed Aug 15 2012 vaci0 <vaci0> 1.3.80-1.mga3
+ Revision: 281443
- Added BuildRequires enchant-devel
-Update to new version 1.3.80

* Fri Jul 27 2012 vaci0 <vaci0> 1.3.6-1.mga3
+ Revision: 274774
- imported package focuswriter

