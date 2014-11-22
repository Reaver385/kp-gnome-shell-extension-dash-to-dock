%global uuid dash-to-dock@micxgx.gmail.com
%global gittag 6a58c86ec6925afab3f40e4a2892cbed6cae8acf

Name:           gnome-shell-extension-dash-to-dock
Version:        0.35
Release:        1.git656e064%{?dist}
Summary:        A dock for the GNOME Shell

License:        GPLv2+
URL:            https://github.com/micheleg/dash-to-dock
Source0:        https://github.com/micheleg/dash-to-dock/archive/%{gittag}.tar.gz

BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  vala-tools
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(upower-glib)

Requires:       gnome-shell >= 3.14.0


%description
A dock for the Gnome Shell. This extension moves the dash out of the overview
transforming it in a dock for an easier launching of applications and a faster
switching between windows and desktops.

%prep
%setup -q -n dash-to-dock-%{gittag}

%install
make install INSTALLBASE=%{buildroot}%{_datadir}/gnome-shell/extensions/ VERSION=%{version}.git%{gittag}

%files
%doc README.md COPYING
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Sun Nov 16 2014 Ian Firns <firnsy@kororproject.org> - 0.35-1.git656e064
- Initial package for Korora
