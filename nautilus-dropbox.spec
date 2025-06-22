%global	_disable_ld_no_undefined 1

Summary:	Dropbox extension for Nautilus
Name:		nautilus-dropbox
Version:		2025.05.20
Release:		2
License:		GPLv2+ and CC-BY-ND
Group:		Graphical desktop/GNOME
Url:		https://getdropbox.com/
Source0:	https://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2
Patch0:		nautilus-dropbox-2025-05.20-fix-env-shebang.patch
Patch1:		nautilus-dropbox-2025-05.20-fix-pkgconfig-name.patch
BuildRequires:		python
BuildRequires:		python-docutils
BuildRequires:		python-gi
BuildRequires:		pkgconfig(glib-2.0)
BuildRequires:		pkgconfig(gtk4)
BuildRequires:		pkgconfig(libnautilus-extension-4)
BuildRequires:		pkgconfig(libnotify)
BuildRequires:		pkgconfig(pygobject-3.0)
BuildRequires:		pkgconfig(python)
BuildRequires:		python3dist(docutils)
Requires:	nautilus
Requires:	dropbox

%description 
Dropbox extension for Nautilus.
It requires proprietary dropbox daemon that will be automatically downloaded
and installed.

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/nautilus/extensions-4/libnautilus-dropbox.so
%{_datadir}/%{name}/*

#--------------------------------------------------------------------

%package -n dropbox
Group:		Networking/File transfer
Summary:	Dropbox client daemon
License:	GPLv2+
Requires:	python-gi
Requires:	python-gpgme
Requires:	wget

%description -n dropbox
Command-line Dropbox client. Currently not all features are realised.
It requires proprietary dropbox daemon to operate. Run `dropbox start -i'
to download and install it automatically.

%files -n dropbox
%license COPYING
%{_bindir}/dropbox
%{_mandir}/man1/dropbox.1.*
%{_datadir}/applications/dropbox.desktop
%{_iconsdir}/hicolor/*/apps/dropbox.png

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
autoreconf -fiv
%configure --disable-static
%make_build


%install
%make_install

# Drop unwanted stuff
rm -f %{buildroot}%{_libdir}/nautilus/extensions-3.0/*.la
rm -f %{buildroot}%{_iconsdir}/hicolor/*/*/*.icon
rm -f %{buildroot}%{_datadir}/%{name}/emblems/*.icon
