#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : audiofile
Version  : 0.3.6
Release  : 23
URL      : https://audiofile.68k.org/audiofile-0.3.6.tar.gz
Source0  : https://audiofile.68k.org/audiofile-0.3.6.tar.gz
Summary  : A library to handle various audio file formats.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: audiofile-bin = %{version}-%{release}
Requires: audiofile-lib = %{version}-%{release}
Requires: audiofile-license = %{version}-%{release}
Requires: audiofile-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : asciidoc
BuildRequires : pkgconfig(flac)
Patch1: 0001-Fix-type-of-test-data-arrays.patch
Patch2: 0002-Fix-warnings-in-tests-comparing-integers-to-enums.patch
Patch3: 0003-Link-with-FLAC-for-static-builds.patch
Patch4: 0004-Fix-undefined-behavior-in-sign-conversion.patch
Patch5: cve-2017-6837.patch
Patch6: cve-2017-6838.patch
Patch7: cve-2017-6839.patch
Patch8: cve-2017-6829.patch
Patch9: cve-2017-6831.patch
Patch10: CVE-2018-13440.patch
Patch11: CVE-2015-7747.patch
Patch12: CVE-2018-17095.patch

%description
The Audio File Library provides an elegant API for accessing a variety
of audio file formats, such as AIFF/AIFF-C, WAVE, and NeXT/Sun
.snd/.au, in a manner independent of file and data formats.

%package bin
Summary: bin components for the audiofile package.
Group: Binaries
Requires: audiofile-license = %{version}-%{release}

%description bin
bin components for the audiofile package.


%package dev
Summary: dev components for the audiofile package.
Group: Development
Requires: audiofile-lib = %{version}-%{release}
Requires: audiofile-bin = %{version}-%{release}
Provides: audiofile-devel = %{version}-%{release}
Requires: audiofile = %{version}-%{release}

%description dev
dev components for the audiofile package.


%package lib
Summary: lib components for the audiofile package.
Group: Libraries
Requires: audiofile-license = %{version}-%{release}

%description lib
lib components for the audiofile package.


%package license
Summary: license components for the audiofile package.
Group: Default

%description license
license components for the audiofile package.


%package man
Summary: man components for the audiofile package.
Group: Default

%description man
man components for the audiofile package.


%package staticdev
Summary: staticdev components for the audiofile package.
Group: Default
Requires: audiofile-dev = %{version}-%{release}

%description staticdev
staticdev components for the audiofile package.


%prep
%setup -q -n audiofile-0.3.6
cd %{_builddir}/audiofile-0.3.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664887431
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%configure
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664887431
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/audiofile
cp %{_builddir}/audiofile-%{version}/COPYING %{buildroot}/usr/share/package-licenses/audiofile/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/audiofile-%{version}/COPYING.GPL %{buildroot}/usr/share/package-licenses/audiofile/4cc77b90af91e615a64ae04893fdffa7939db84c || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sfconvert
/usr/bin/sfinfo

%files dev
%defattr(-,root,root,-)
/usr/include/af_vfs.h
/usr/include/audiofile.h
/usr/include/aupvlist.h
/usr/lib64/libaudiofile.so
/usr/lib64/pkgconfig/audiofile.pc
/usr/share/man/man3/afCloseFile.3
/usr/share/man/man3/afGetDataOffset.3
/usr/share/man/man3/afGetFrameCount.3
/usr/share/man/man3/afGetFrameSize.3
/usr/share/man/man3/afGetTrackBytes.3
/usr/share/man/man3/afInitAESChannelData.3
/usr/share/man/man3/afInitAESChannelDataTo.3
/usr/share/man/man3/afInitByteOrder.3
/usr/share/man/man3/afInitChannels.3
/usr/share/man/man3/afInitCompression.3
/usr/share/man/man3/afInitFileFormat.3
/usr/share/man/man3/afInitRate.3
/usr/share/man/man3/afInitSampleFormat.3
/usr/share/man/man3/afNewFileSetup.3
/usr/share/man/man3/afOpenFile.3
/usr/share/man/man3/afQuery.3
/usr/share/man/man3/afQueryDouble.3
/usr/share/man/man3/afQueryLong.3
/usr/share/man/man3/afQueryPointer.3
/usr/share/man/man3/afReadFrames.3
/usr/share/man/man3/afReadMisc.3
/usr/share/man/man3/afSeekFrame.3
/usr/share/man/man3/afSeekMisc.3
/usr/share/man/man3/afSetErrorHandler.3
/usr/share/man/man3/afSetVirtualByteOrder.3
/usr/share/man/man3/afSetVirtualChannels.3
/usr/share/man/man3/afSetVirtualPCMMapping.3
/usr/share/man/man3/afSetVirtualSampleFormat.3
/usr/share/man/man3/afTellFrame.3
/usr/share/man/man3/afWriteFrames.3
/usr/share/man/man3/afWriteMisc.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaudiofile.so.1
/usr/lib64/libaudiofile.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/audiofile/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/audiofile/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sfconvert.1
/usr/share/man/man1/sfinfo.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libaudiofile.a
