# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       libngf-qt5

# >> macros
# << macros

Summary:    Qt-based client library for Non-Graphic Feedback daemon
Version:    0.2
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        https://github.com/nemomobile/libngf-qt
Source0:    %{name}-%{version}.tar.bz2
Source100:  libngf-qt5.yaml
Requires:   ngfd
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  doxygen

%description
This package contains the Qt-based client library for accessing
Non-graphic feedback services.


%package devel
Summary:    Development package for Qt-based client library for NGF daemon
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package declarative
Summary:    Declarative plugin for NGF clients
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description declarative
%{summary}.

%package tests
Summary:    Test suite for libngf-qt5
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libngf-qt5.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/libngf-qt5.so
%{_includedir}/ngf-qt5/*.h
%{_includedir}/ngf-qt5/NgfClient
%{_libdir}/pkgconfig/ngf-qt5.pc
# >> files devel
# << files devel

%files declarative
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/ngf/*
# >> files declarative
# << files declarative

%files tests
%defattr(-,root,root,-)
/opt/tests/libngf-qt5/*
# >> files tests
# << files tests
