Summary:	Flat theme without distracting stuff
Summary(pl.UTF-8):	Płaski motyw bez zbędnych drobiazgów
Name:		gtk2-theme-engine-Flat
Version:	2.0
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gtk2/GTK2-Flat-Engine.tar.gz
# Source0-md5:	a4d6866a518f05087bd7aef43a55432a
URL:		http://art.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This theme engine gives gtk+2 a flattened appearance with elements
taken from the MacOS and Metal uis. Modified from the default and
metal theme engines; the colors and background pixmaps are fully
customizable.

%description -l pl.UTF-8
Ten motyw daje bibliotece gtk+2 płaski wygląd z elementami wziętymi z
interfejsów MacOS i Metal. Jest zmodyfikowany w stosunku do domyślnego
i metalowego motywu; kolory i pixmapy tła są w pełni konfigurowalne.

%prep
%setup  -q -n gtk-flat-theme-%{version}

%build
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

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/Flat
