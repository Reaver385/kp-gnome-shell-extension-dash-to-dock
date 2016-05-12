%global uuid dash-to-dock@micxgx.gmail.com
#%global gittag 6a58c86ec6925afab3f40e4a2892cbed6cae8acf
#%global gittag 8d2ccc73b79a483126bd1b23e6fe0de356dd7c73
#%global gittag 91e7913649c15592a9c54b277f8056d8cd9bd786
#%global gittag 2b48c5b04f9d485072df76f96dcce84c14047dd4
#%global gitshorttag 2b48c5b
#%global gittag e80e7cf5f0e46f78883291bff8362a748fec3290
#%global gitshorttag e80e7cf
%global gittag ef68847834f053dcd117cba889da6efe37471a48
%global gitshorttag ef68847


Name:           gnome-shell-extension-dash-to-dock
Version:        0.50
Release:        1.git%{gitshorttag}%{?dist}
Summary:        A dock for the GNOME Shell

License:        GPLv2+
URL:            https://github.com/micheleg/dash-to-dock
Source0:        https://github.com/micheleg/dash-to-dock/archive/%{gittag}.tar.gz
Patch0:         korora-schema-defaults.patch

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
Requires(post): glib2


%description
A dock for the Gnome Shell. This extension moves the dash out of the overview
transforming it in a dock for an easier launching of applications and a faster
switching between windows and desktops.

%prep
%setup -q -n dash-to-dock-%{gittag}
%patch0 -p1

%install
make install INSTALLBASE=%{buildroot}%{_datadir}/gnome-shell/extensions/ VERSION=%{version}.git%{gittag}

mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 %{_builddir}/dash-to-dock-%{gittag}/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ 2>/dev/null

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ 2>/dev/null

%files
%doc README.md COPYING
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Mon Feb 22 2016 Chris Smart <csmart@kororproject.org> - 0.52-1.gite80e7cf
- Bump to latest upstream version.

* Thu Oct 08 2015 Chris Smart <csmart@kororproject.org> - 0.49-1.git2b48c5b
- Bump to latest upstream version.

* Wed Jul 15 2015 Ian Firns <firnsy@kororproject.org> - 0.46.1-2.git91e7913
- Patch our defaults straight into the plugin.

* Thu Jun  4 2015 Ian Firns <firnsy@kororproject.org> - 0.46.1-1.git91e7913
- Updated to latest upstream.

* Thu Jan  8 2015 Ian Firns <firnsy@kororproject.org> - 0.35.1-2.git8d2ccc7
- Install gschema

* Sun Nov 16 2014 Ian Firns <firnsy@kororproject.org> - 0.35.1-1.git8d2ccc7
- Update to lastest upstream release

* Sun Nov 16 2014 Ian Firns <firnsy@kororproject.org> - 0.35-1.git656e064
- Initial package for Korora
