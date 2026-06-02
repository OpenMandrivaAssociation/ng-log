%if ! %{cross_compiling}
%define __cc %{_bindir}/gcc
%define __cxx %{_bindir}/g++
%endif

%define major 1
%define libnglog %mklibname ng-log
%define libnglog_devel %mklibname ng-log -d
%define libglog %mklibname glog
%define libglog_devel %mklibname glog -d

Name:      ng-log
Version:   0.8.2
Release:   1

License:   BSD

# Originally https://github.com/google/glog -- abandoned 2025

URL:       https://github.com/ng-log/ng-log
Source0:   https://github.com/ng-log/ng-log/archive/refs/tags/v%{version}.tar.gz

Summary: Logging library for C++
Group:   Development/C++

BuildSystem:	cmake
%rename glog

%description
The ng-log (formerly glog) library implements application-level logging. This library provides
logging APIs based on C++-style streams and various helper macros.

#------------------------------------------------------------------------------#

%package -n %{libnglog}

Summary: Logging library for C++
Group:   Development/C++

Provides: %{name} = %{version}
Provides: glog = %{version}
%rename %{libglog}

%if "%{_lib}" == "lib64"
Provides: libglog.so.3()(64bit)
%else
Provides: libglog.so.3
%endif

%description -n %{libnglog}
The ng-log (formerly glog) library implements application-level logging. This library provides
logging APIs based on C++-style streams and various helper macros.

%files -n %{libnglog}
%{_libdir}/libglog.so.*
%{_libdir}/libng-log.so.*

#------------------------------------------------------------------------------#

%package -n %{libnglog_devel}

Summary: Development files for %{libglog}
Group:   Development/C++

%rename %{libglog_devel}
Requires: %{libnglog} = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: libglog-devel = %{version}-%{release}

%description -n %{libnglog_devel}
Development files for %{libglog}

%files -n %{libnglog_devel}
%{_libdir}/libglog.so
%{_libdir}/libng-log.so
%{_includedir}/glog
%{_includedir}/ng-log
%{_libdir}/cmake/glog
%{_libdir}/cmake/ng-log
