Name:           libdxfrw
Version:        0.5.11
Release:        1%{?dist}
Summary:        Library to read and write DXF files in ascii and binary form

License:        GPLv2+
URL:            http://sourceforge.net/projects/libdxfrw/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  libtool


%description
This C++ library is a free library to read and write DXF files
in both formats, ascii and binary form.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS"
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc TODO README NEWS COPYING AUTHORS
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Jan 23 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.11-1
- Initial version for Fedora
