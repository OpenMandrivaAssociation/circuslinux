%define name circuslinux
%define version 1.0.3
%define release %mkrel 16

Summary: Cute breakout-like game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.sonic.net/pub/users/nbs/unix/x/circus-linux/circuslinux-%{version}.tar.bz2
Source5: %{name}-16.png
Source6: %{name}-32.png
Source7: %{name}-48.png
Patch0: %{name}-1.0.3-fix-64bits-build.patch
License: GPLv2
Url: http://newbreedsoftware.com/circus-linux/
Group: Games/Arcade
BuildRequires:	SDL_image-devel
BuildRequires:	libalsa-devel
BuildRequires:	esound-devel
BuildRequires:	texinfo
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
"Circus Linux!" is based on the Atari 2600 game "Circus Atari" by Atari,
released in 1980.  Gameplay is similar to "Breakout" and "Arkanoid"- you
slide a device left and right to bounce objects into the air which destroy
a wall.

%prep
%setup -q
%patch0 -p1

# fix EOL
mv README-SDL.txt README-SDL.txt.msdos
sed -e 's/\r$//' README-SDL.txt.msdos > README-SDL.txt

cat << EOF > mandriva-%{name}.desktop
[Desktop Entry]
Name=Circus Linux
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall bindir=$RPM_BUILD_ROOT%{_gamesbindir} datadir=$RPM_BUILD_ROOT%{_gamesdatadir}

install -D -m644 mandriva-%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
install -D -m644 %SOURCE6 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE6 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D -m644 %SOURCE5 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE5 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D -m644 %SOURCE7 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m644 %SOURCE7 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

rm -rf %buildroot%_datadir/doc/circuslinux-1.0.3

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS.txt CHANGES.txt README.txt FAQ.txt README-SDL.txt
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png


%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 1.0.3-16mdv2011.0
+ Revision: 571835
- use configure2_5x

* Fri Jun 12 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 1.0.3-16mdv2010.0
+ Revision: 385534
- fix build on x86_64
- fix EOL in README-SDL.txt
- fix license

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.0.3-13mdv2009.0
+ Revision: 218434
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-13mdv2008.1
+ Revision: 149049
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.3-12mdv2008.0
+ Revision: 41210
- clean buildrequires; drop old menu; drop X-Mandriva XDG category; rebuild for 2008
- drop old menu; drop X-Mandriva XDG category; fd.o icons; rebuild for 2008
- Import circuslinux



* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 1.0.3-11mdv2007.0
- use mkrel
- switch to XDG menu

* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 1.0.3-10mdk
- rebuild for sparc

* Tue Oct 11 2005 Pixel <pixel@mandriva.com> 1.0.3-9mdk
- rebuild

* Fri Aug 13 2004 Pixel <pixel@mandrakesoft.com> 1.0.3-8mdk
- rebuild

* Tue Jul 22 2003 Per ÿyvind Karlsen <peroyvind@sintrax.net> 1.0.3-7mdk
- rebuild
- really remove Prefix tag
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- change icons
- use %%{_gamesdatadir}
- cosmetics

* Fri Nov 08 2002 Per ÿyvind Karlsen <peroyvind@delonic.no> 1.0.3-6mdk
- Removed gcc, automake and autoconf from BuildRequires and also removed Prefix,
  no need for this
- Added missing install stage
- Added menuitem
- Added icons
- Moved binary into %%{_gamesbindir}
- Quiet setup

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.3-5mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.3-4mdk
- Automated rebuild with gcc3.2

* Sun Jul 21 2002 Pixel <pixel@mandrakesoft.com> 1.0.3-3mdk
- recompile against new vorbis stuff

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 1.0.3-2mdk
- rebuild for new libasound (alsa)

* Sat Feb  2 2002 Pixel <pixel@mandrakesoft.com> 1.0.3-1mdk
- new release

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu> 1.0.1-9mdk
- BuildRequires

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 1.0.1-8mdk
- rebuilding for libpng3

* Fri Sep 28 2001 Stefan van der Eijk <stefan@eijk.nu> 1.0.1-7mdk
- BuildRequires:	libSDL-devel libSDL_image-devel

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 1.0.1-6mdk
- rebuild

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 1.0.1-5mdk
- rebuild with new SDL

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-4mdk
- rebuild for new libSDL_mixer

* Wed Nov  8 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-3mdk
- capitalize summary

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-2mdk
- rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-1mdk
- initial spec


# end of file
