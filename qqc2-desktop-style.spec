Summary: QtQuickControls2 style for consistency between QWidget and QML apps 
Name: qqc2-desktop-style
Version: 5.116.1
Release: 1
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
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_MESSAGES/qqc2desktopstyle5_qt.qm
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/qqc2desktopstyle5_qt.qm
