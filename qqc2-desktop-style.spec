Summary: QtQuickControls2 style for consistency between QWidget and QML apps 
Name: qqc2-desktop-style
Version: 5.74.0
Release: 2
License: GPLv3
URL: http://kde.org/
Group: System/Libraries
Source0: http://download.kde.org/stable/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Kirigami2) >= %(echo %{version} |cut -d. -f1-2).0
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5DBus)
Requires: qt5-qtquickcontrols2

%description
This is a style for QtQuickControls 2 that uses QWidget's QStyle for
painting, making possible to achieve an higher degree of consistency
between QWidget-based and QML-based apps.

%package devel
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{name} >= %{EVRD}

%description devel
Development files for %{name}.

%files devel
%{_libdir}/cmake/KF5QQC2DeskopStyle
%{_libdir}/cmake/KF5QQC2DesktopStyle

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%dir %{_libdir}/qt5/plugins/kf5/kirigami
%{_libdir}/qt5/plugins/kf5/kirigami/org.kde.desktop.so
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.desktop
%{_libdir}/qt5/qml/org/kde/qqc2desktopstyle
