Summary:	Dropbox extension for Nautilus
Name:		nautilus-dropbox
Version: 	2018.11.28
Release: 	1
Source0:	http://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2
# Currently all images in package are licensed under CC BY-ND, so third-party files are not needed
#Source1:	http://fc04.deviantart.com/fs39/f/2008/356/b/9/b9722db2a11fa3092f3b902b681866a9.zip
#Source2:	emblem-syncing.png
#Source3:	emblem-unsyncable.png
#Source4:	emblem-uptodate.png
License: 	GPLv2+ and CC-BY-ND
Group: 		Graphical desktop/GNOME
Url: 		http://getdropbox.com/

BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	python-docutils
BuildRequires:  pkgconfig(python)
BuildRequires:  python
Requires:	nautilus
Requires:	dropbox


%description 
Dropbox extension for Nautilus.

It requires proprietary dropbox daemon that will be automatically downloaded
and installed.


%files
%doc AUTHORS
%doc COPYING
%doc README
%_libdir/nautilus/extensions-3.0/libnautilus-dropbox.so
%_datadir/%name/*

#--------------------------------------------------------------------

%package -n dropbox
Group:		Networking/File transfer
Summary:	Dropbox client daemon
License:	GPLv2+

%description -n dropbox
Command-line Dropbox client. Currently not all features are realised.

It requires proprietary dropbox daemon to operate. Run `dropbox start -i'
to download and install it automatically.

%files -n dropbox
%doc AUTHORS
%_bindir/*
%_mandir/man1/*
%_datadir/applications/dropbox.desktop
%_iconsdir/hicolor/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install

rm -f %buildroot%_libdir/nautilus/extensions-3.0/*.la
rm -f %buildroot%_iconsdir/hicolor/*/*/*.icon
rm -f %buildroot%_datadir/nautilus-dropbox/emblems/*.icon
