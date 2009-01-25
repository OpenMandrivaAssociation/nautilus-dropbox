Name: 		nautilus-dropbox
Summary: 	Secure backup,sync and sharing made easy
Version: 	0.5.0
Release: 	%mkrel 1
License: 	GPLv2
Group: 		Graphical desktop/GNOME
Source: 	%{name}-%{version}.tar.bz2
Url:		http://getdropbox.com

BuildRequires:	nautilus-devel libnotify-devel
Requires:	nautilus

BuildRoot: %{_tmppath}/build-root-%{name}

%description
A handy tool that can be used either in a GUI or on the commandline to backup, sync and share files.

%prep
%setup -q

%build

%configure2_5x
%make

%install
%makeinstall_std

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_libdir}/nautilus/extensions-2.0/libnautilus-dropbox.a
%{_libdir}/nautilus/extensions-2.0/libnautilus-dropbox.la
%{_libdir}/nautilus/extensions-2.0/libnautilus-dropbox.so
%{_datadir}/icons/hicolor/16x16/apps/dropbox.png
%{_datadir}/icons/hicolor/64x64/emblems/emblem-dropbox-syncing.icon
%{_datadir}/icons/hicolor/64x64/emblems/emblem-dropbox-syncing.png
%{_datadir}/icons/hicolor/64x64/emblems/emblem-dropbox-uptodate.icon
%{_datadir}/icons/hicolor/64x64/emblems/emblem-dropbox-uptodate.png
%{_datadir}/icons/hicolor/64x64/emblems/emblem-dropbox-unsyncable.icon
%{_datadir}/icons/hicolor/64x64/emblems/emblem-dropbox-unsyncable.png
