Summary:	inotify "tail"
Name:		inotail
Version:	0.5
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://distanz.ch/inotail/%{name}-%{version}.tar.bz2
# Source0-md5:	82d4d05f86d6069e95c4b73e4004f15f
Patch0:		%{name}-Makefile.patch
URL:		http://distanz.ch/inotail/
Requires:	uname(release) >= 2.6.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
inotail is a replacement for the 'tail' program found in the base
installation of every Linux/UNIX system. It makes use of the inotify
infrastructure in recent versions of the Linux kernel to speed up tailing
files in the follow mode (the '-f' option). Standard tail polls the file
every second by default while inotail listens to special events sent by the
kernel through the inotify API to determine whether a file needs to be
reread.

Currently inotail is not fully compatible to neither POSIX or GNU tail but
might be in the future.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR="$RPM_BUILD_ROOT%{_bindir}" \
	MANDIR="$RPM_BUILD_ROOT%{_mandir}/man1"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
