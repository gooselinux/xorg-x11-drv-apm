%define tarball xf86-video-apm
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers

Summary:   Xorg X11 apm video driver
Name:      xorg-x11-drv-apm
Version: 1.2.2
Release: 1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   apm.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6

Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6
Requires:  hwdata

%description 
X.Org X11 apm video driver.

%prep

%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/apm_drv.so
%{_datadir}/hwdata/videoaliases/apm.xinf
%{_mandir}/man4/apm.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.2-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 1.2.2-1
- rebase to new upstream releae 1.2.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.2.1-3.1
- ABI bump

* Mon Jun 22 2009 Adam Jackson <ajax@redhat.com> 1.2.1-3
- Fix ABI for new server

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.2.1-1
- upgrade to latest upstream release

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.2.0-2
- rebuild for server API change

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.2.0-1
- Upgrade to latest upstream release

* Tue Mar 11 2008 Dave Airlie <airlied@redhat.com> 1.1.1-9
- pciaccess conversion

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.1-8
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.1.1-7
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.1.1-6
- Update Requires and BuildRequires.

* Sat May 26 2007 Adam Jackson <ajax@redhat.com> 1.1.1-5
- Yet more merge review changes. (#226577)

* Thu May 24 2007 Adam Jackson <ajax@redhat.com> 1.1.1-4
- Merge review changes. (#226577)

* Thu Feb 15 2007 Adam Jackson <ajax@redhat.com> 1.1.1-3
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-1
- Update to 1.1.1 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1.5-1
- Updated xorg-x11-drv-apm to version 1.0.1.5 from X11R7.0
- Added apm.xinf videoalias file.

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.1.4-1
- Updated xorg-x11-drv-apm to version 1.0.1.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.1.2-1
- Updated xorg-x11-drv-apm to version 1.0.1.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.0.1.1-1
- Updated xorg-x11-drv-apm to version 1.0.1.1 from X11R7 RC1
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Set "ExclusiveArch: %%{ix86}" to match what was shipped in previous OS
  releases.

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for apm video driver generated automatically
  by my xorg-driverspecgen script.
