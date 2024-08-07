%define _disable_ld_no_undefined 1

Summary:	Dropbox extension for Nautilus
Name:		nautilus-dropbox
Version: 	2024.04.17
Release: 	1
Source0:	https://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2
License: 	GPLv2+ and CC-BY-ND
Group: 		Graphical desktop/GNOME
Url: 		https://getdropbox.com/
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:	python3dist(docutils)
BuildRequires:  pkgconfig(python)
BuildRequires:  python
BuildRequires:  python-gi
Requires:	nautilus
Requires:	dropbox

%description 
Dropbox extension for Nautilus.

It requires proprietary dropbox daemon that will be automatically downloaded
and installed.

%files
%doc AUTHORS
%doc COPYING
%{_libdir}/nautilus/extensions-4/libnautilus-dropbox.so
%{_datadir}/%name/*
#--------------------------------------------------------------------

%package -n dropbox
Group:		Networking/File transfer
Summary:	Dropbox client daemon
License:	GPLv2+
Requires: python-gpg
Requires:	wget
Requires:	python-gi

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
%autopatch -p1

autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install

rm -f %buildroot%_libdir/nautilus/extensions-3.0/*.la
rm -f %buildroot%_iconsdir/hicolor/*/*/*.icon
rm -f %buildroot%_datadir/nautilus-dropbox/emblems/*.icon
