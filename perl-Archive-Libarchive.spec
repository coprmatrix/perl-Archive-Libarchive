#
# spec file for package perl-Archive-Libarchive (Version 0.08)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name Archive-Libarchive
Name:           perl-Archive-Libarchive
Version:        0.08
Release:        0
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Modern Perl bindings to libarchive
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  (rpm-build-perl or perl-generators)
BuildRequires:  perl(FFI::C::File)
BuildRequires:  perl(FFI::CheckLib) >= 0.30
BuildRequires:  perl(FFI::C::Stat)
BuildRequires:  perl(FFI::Platypus) >= 1.38
BuildRequires:  perl(FFI::Platypus::Type::Enum) >= 0.05
BuildRequires:  perl(FFI::Platypus::Type::PtrObject)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Term::Table)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Tools::MemoryCycle)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Archive::Libarchive)
BuildRequires:  perl(Test::Script) >= 1.09
Requires:       perl(FFI::CheckLib) >= 0.30
Requires:       perl(FFI::C::Stat)
Requires:       perl(FFI::Platypus) >= 1.38
Requires:       perl(FFI::Platypus::Type::Enum) >= 0.05
Requires:       perl(FFI::Platypus::Type::PtrObject)
Requires:       perl(Ref::Util)
Requires:       libarchive-devel


%description
This module provides a Perl object-oriented interface to the 'libarchive'
library. The 'libarchive' library is the API used to implemnt 'bsdtar', the
default tar implementation on a number of operating systems, including
FreeBSD, macOS and Windows. It can also be installed on most Linux
distributions. But wait, there is more, 'libarchive' supports a number of
formats, compressors and filters transparently, so it can be a useful when
used as a universal archiver/extractor. Supported formats include:

* various tar formats, including the oldest forms and the newest extensions

* zip

* ISO 9660 (CD-ROM image format)

* gzip

* bzip2

* uuencoded files

* shell archive (shar)

* ... and many many more

There are a number of "simple" interfaces around this distribution, which
are worth considering if you do not need the full power and configurability
that this distribution provides.

* Archive::Libarchive::Peek

Provides an interface for listing and retrieving entries from an archive
without extracting them to the local filesystem.

* Archive::Libarchive::Extract

Provides an interface for extracting arbitrary archives of any
format/filter supported by 'libarchive'.

* Archive::Libarchive::Unwrap

Decompresses / unwraps files that have been compressed or wrapped in any of
the filter formats supported by 'libarchive'

This distribution is split up into several classes, that correspond to
'libarchive' classes. Probably the best place to start when learning how to
use this module is to look at the EXAMPLES section below, but you can also
take a look at the main class documentation for the operation that you are
interested in as well:

* Archive => Archive::Libarchive::ArchiveRead

Class for reading from archives.

* Archive => Archive::Libarchive::ArchiveWrite

Class for creating new archives.

* Archive => ArchiveRead => Archive::Libarchive::DiskRead

Class for reading file entries from a local filesystem.

* Archive => ArchiveWrite => Archive::Libarchive::DiskWrite

Class for writing file entries to a local filesystem.

* Archive::Libarchive::Entry

Class representing file metadata of a file inside an archive, or in the
local filesystem.

* Archive::Libarchive::EntryLinkResolver

This is the 'libarchive' link resolver API.

* Archive =>  Archive::Libarchive::Match

This is the 'libarchive' match API.

This module attempts to provide comprehensive bindings to the 'libarchive'
library. For more details on the history and alternatives to this project
see the HISTORY section below. All recent versions of 'libarchive' should
be supported, although some methods are only available when you have the
most recent version of 'libarchive' installed. For methods not available on
older versions please consult Archive::Libarchive::API, which will list
these methods as '(optional)'. If you need to support both older versions
of 'libarchive' and exploit the newer methods on newer versions of
'libarchive' you can use the 'can' method to check if they are available.
If you need the latest version of 'libarchive', and your system provides an
older version, then you can force a 'share' install of Alien::Libarchive3:

 env ALIEN_INSTALL_TYPE=share cpanm Alien::Libarchive3

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README
%license LICENSE

%changelog
