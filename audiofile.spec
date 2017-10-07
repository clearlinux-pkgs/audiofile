#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : audiofile
Version  : 0.3.6
Release  : 6
URL      : http://audiofile.68k.org/audiofile-0.3.6.tar.gz
Source0  : http://audiofile.68k.org/audiofile-0.3.6.tar.gz
Summary  : A library to handle various audio file formats.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: audiofile-bin
Requires: audiofile-lib
Requires: audiofile-doc
BuildRequires : alsa-lib-dev
BuildRequires : pkgconfig(flac)
Patch1: 0001-Fix-type-of-test-data-arrays.patch
Patch2: 0002-Fix-warnings-in-tests-comparing-integers-to-enums.patch
Patch3: 0003-Link-with-FLAC-for-static-builds.patch
Patch4: 0004-Fix-undefined-behavior-in-sign-conversion.patch
Patch5: cve-2017-6837.patch
Patch6: cve-2017-6838.patch
Patch7: cve-2017-6839.patch
Patch8: cve-2017-6832.nopatch
Patch9: cve-2017-6833.nopatch
Patch10: cve-2017-6834.nopatch
Patch11: cve-2017-6835.nopatch
Patch12: cve-2017-6836.nopatch
Patch13: cve-2017-6827.nopatch
Patch14: cve-2017-6828.nopatch
Patch15: cve-2017-6829.patch
Patch16: cve-2017-6830.nopatch
Patch17: cve-2017-6831.patch

%description
The Audio File Library provides an elegant API for accessing a variety
of audio file formats, such as AIFF/AIFF-C, WAVE, and NeXT/Sun
.snd/.au, in a manner independent of file and data formats.

%package bin
Summary: bin components for the audiofile package.
Group: Binaries

%description bin
bin components for the audiofile package.


%package dev
Summary: dev components for the audiofile package.
Group: Development
Requires: audiofile-lib
Requires: audiofile-bin
Provides: audiofile-devel

%description dev
dev components for the audiofile package.


%package doc
Summary: doc components for the audiofile package.
Group: Documentation

%description doc
doc components for the audiofile package.


%package lib
Summary: lib components for the audiofile package.
Group: Libraries

%description lib
lib components for the audiofile package.


%prep
%setup -q -n audiofile-0.3.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch15 -p1
%patch17 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507400543
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507400543
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sfconvert
/usr/bin/sfinfo

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.a
/usr/lib64/libaudiofile.so
/usr/lib64/pkgconfig/audiofile.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaudiofile.so.1
/usr/lib64/libaudiofile.so.1.0.0
