Summary:	Flat theme without distracting stuff
Summary(pl):	P³aski temat bez zbêdnych drobiazgów
Name:		gtk2-theme-engine-Flat
Version:	2.0
Release:	0.1
License:	GPL
Group:		Themes/Gtk
Source0:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gtk2/GTK2-Flat-Engine.tar.gz
URL:		http://art.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
This theme engine gives gtk+ a flattened appearance with elements
taken from the MacOS and Metal uis. Modified from the default and
metal theme engines; the colors and background pixmaps are fully
customizable.

%prep
%setup  -q -n gtk-flat-theme-%{version}

%build
rm -f missing
%{__libtoolize}
aclocal
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
%attr(755,root,root) %{_libdir}/gtk-2.0/2.0.*/engines/*.so
%{_datadir}/themes/Flat
