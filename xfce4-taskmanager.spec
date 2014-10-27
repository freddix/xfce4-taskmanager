Summary:	Task manager for XFCE Desktop
Name:		xfce4-taskmanager
Version:	1.0.1
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-taskmanager/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	b8a707b25e32c1a296eb50d609aa49b8
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Task manager for XFCE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop

