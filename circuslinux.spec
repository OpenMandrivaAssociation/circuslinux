%define name circuslinux
%define version 1.0.3
%define release %mkrel 12

Summary: Cute breakout-like game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.sonic.net/pub/users/nbs/unix/x/circus-linux/circuslinux-%{version}.tar.bz2
Source5: %{name}-16.png
Source6: %{name}-32.png
Source7: %{name}-48.png
License: GPL
Url: http://newbreedsoftware.com/circus-linux/
Group: Games/Arcade
BuildRequires:	SDL_image-devel
BuildRequires:	libalsa-devel
BuildRequires:	esound-devel
BuildRequires:	texinfo

%description
"Circus Linux!" is based on the Atari 2600 game "Circus Atari" by Atari,
released in 1980.  Gameplay is similar to "Breakout" and "Arkanoid"- you
slide a device left and right to bounce objects into the air which destroy
a wall.

%prep
%setup -q

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

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

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
