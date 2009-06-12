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
%ifarch x86_64
Patch0: %{name}-1.0.3-fix-64bits-build.patch
%endif
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
%ifarch x86_64
%patch0 -p1
%endif

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
%configure	--bindir=%{_gamesbindir} \
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
