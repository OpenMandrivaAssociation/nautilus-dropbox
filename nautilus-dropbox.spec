Summary:	Dropbox extension for Nautilus
Name:		nautilus-dropbox
Version: 	0.5.0
Release: 	%mkrel 2
Source0: 	http://linux.getdropbox.com/packages/%name-%version.tar.bz2
# Icons in Source0 is not free, so we are using icons from here (CC-BY-ND license):
# http://vathanx.deviantart.com/art/Dropbox-Icon-106941298
Source1:	http://fc04.deviantart.com/fs39/f/2008/356/b/9/b9722db2a11fa3092f3b902b681866a9.zip
# Source2,3,4 from here: http://www.iconspedia.com/pack/vistoon-145/
Source2:	emblem-syncing.png
Source3:	emblem-unsyncable.png
Source4:	emblem-uptodate.png
License: 	GPLv2+ and CC-BY-ND
Group: 		Graphic desktop/GNOME
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	nautilus-devel libnotify-devel
Requires:	nautilus wget

%description 
Dropbox extension for Nautilus.

%files
%defattr(-,root,root)
%_libdir/nautilus/extensions-2.0/libnautilus-dropbox.so
%_iconsdir/hicolor/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -a1
cp -f "Dropbox Icon/PNG/Dropbox 16.png" dropbox.png
cp %{SOURCE2} emblem-dropbox-syncing.png
cp %{SOURCE3} emblem-dropbox-unsyncable.png
cp %{SOURCE4} emblem-dropbox-uptodate.png

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

rm -f %buildroot%_libdir/nautilus/extensions-2.0/*.la
rm -f %buildroot%_iconsdir/hicolor/*/*/*.icon

%clean
rm -rf %{buildroot}
