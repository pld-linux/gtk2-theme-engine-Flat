Summary:	Flat theme without distracting stuff
Summary(pl):	P³aski motyw bez zbêdnych drobiazgów
Name:		gtk2-theme-engine-Flat
Version:	2.0
Release:	0.1
License:	GPL
Group:		Themes/Gtk
Source0:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gtk2/GTK2-Flat-Engine.tar.gz
# Source0-md5:	a4d6866a518f05087bd7aef43a55432a
URL:		http://art.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This theme engine gives gtk+ a flattened appearance with elements
taken from the MacOS and Metal uis. Modified from the default and
metal theme engines; the colors and background pixmaps are fully
customizable.

%description -l pl
Ten motyw daje bibliotece gtk+ p³aski wygl±d z elementami wziêtymi z
interfejsów MacOS i Metal. Jest zmodyfikowany w stosunku do domy¶lnego
i metalowego motywu; kolory i pixmapy t³a s± w pe³ni konfigurowalne.

%prep
%setup  -q -n gtk-flat-theme-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/gtk-2.0/2.2.*/engines/*.so
%{_libdir}/gtk-2.0/2.2.*/engines/*.la
%{_datadir}/themes/Flat
