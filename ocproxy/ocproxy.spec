# 
# ocproxy spec file
#

Name: ocproxy
Summary: ownCloud Proxy
Version: 0.0.52
Release: 1%{?dist}
License: AGPLv3
BuildRoot: %{_tmppath}/%{name}-buildroot
Group: CERN-IT/ST
BuildArch: x86_64
Source: %{name}-%{version}.tar.gz

%description
This RPM provides an ownCloud Proxy for CERNBox REVA daemon.

# Don't do any post-install weirdness, especially compiling .py files
%define __os_install_post %{nil}

%prep
%setup -n %{name}-%{version}

%install
# server versioning

# installation
rm -rf %buildroot/
mkdir -p %buildroot/usr/local/bin
mkdir -p %buildroot/etc/ocproxy
mkdir -p %buildroot/etc/logrotate.d
mkdir -p %buildroot/usr/lib/systemd/system
mkdir -p %buildroot/var/log/ocproxy
install -m 755 ocproxy	     %buildroot/usr/local/bin/ocproxy
install -m 644 ocproxy.service    %buildroot/usr/lib/systemd/system/ocproxy.service
install -m 644 ocproxy.yaml       %buildroot/etc/ocproxy/ocproxy.yaml
install -m 644 ocproxy.logrotate  %buildroot/etc/logrotate.d/ocproxy

%clean
rm -rf %buildroot/

%preun

%post

%files
%defattr(-,root,root,-)
/etc/ocproxy
/etc/logrotate.d/ocproxy
/var/log/ocproxy
/usr/lib/systemd/system/ocproxy.service
/usr/local/bin/*
%config(noreplace) /etc/ocproxy/ocproxy.yaml


%changelog
* Wed Jul 25 2019 Diogo Castro <diogo.castro@cern.ch> 0.0.52
- Mock search endpoint to avoid going to OC
- Fix CERNBox webpage url in download templates
- BaseURL to allow deployment in ScienceBox
- Publick links without access except when password share
* Wed Jul 10 2019 Diogo Castro <diogo.castro@cern.ch> 0.0.51
- Send share emails as the user
- Cleanup templates
* Thu Jun 20 2019 Diogo Castro <diogo.castro@cern.ch> 0.0.50
- Fail when unable to get chunk for download of file
- Add gantt support
- Add onlyoffice support
* Tue May 27 2019 Diogo Castro <diogo.castro@cern.ch> 0.0.49
- Fixes for canary mode (set/clean cookie)
- Revert public links without access token
* Tue May 21 2019 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.48
- Support ZIP downloads for archives
- Support director download of public links
- Allow listing recycle entries by date range
- Add canary mode support
- Minor fixes: content-length, content-disposition on downloads
* Tue Apr 30 2019 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.47
- Add configurable thumbnails folder
* Fri Mar 22 2019 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.46
- Fix path remap for new projects from Share with others
* Fri Mar 22 2019 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.45
- Fix migration logic for projects
* Thu Mar 21 2019 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.44
- Support project space migration
* Tue Mar 05 2019 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.43
- Fix image preview aspect ratio 
* Mon Feb 18 2019 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.42
- Add restart=always to systemd
* Thu Dec 13 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.41
- Support VSDX and VSD files
* Tue Dec 03 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.40
- Allow non-password protected links to be directly downloaded
* Tue Nov 20 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.39
- Add random uuid to files uploaded using the drop zone
* Tue Nov 20 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.38
- Fix HTML footer for drop zone
* Mon Nov 19 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.37
- Add drop-only support for public links
* Mon Nov 12 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.36
- Add ROOT Viewer support
* Fri Nov 9 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.35
- Fix get quota response
* Thu Oct 25 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.34
- Enable cache for shared with you only
* Thu Oct 25 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.33
- Add support to filter shares by path and disable share cache
* Thu Oct 18 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.32
- Fix handling of colon prefixes in the mounts
* Thu Oct 10 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.31
- Improve mail message with link to share
* Thu Oct 10 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.30
- Add decline share functionality
* Tue Oct 09 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.29
- Add DrawIO support
* Tue Oct 09 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.28
* Tue Oct 09 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.27
- Add mail support
* Thu Sep 27 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.26
* Thu Sep 27 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.25
* Wed Sep 26 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.24
- Fix drawIO connection url
* Wed Sep 26 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.23
* Mon Sep 17 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.22
* Tue Aug 28 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.21
* Fri Aug 24 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.20
* Fri Aug 24 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.19
* Wed Aug 21 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.18
* Tue Aug 21 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.17
* Mon Aug 20 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.16
* Fri Aug 17 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.15
* Thu Aug 16 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.14
* Thu Aug 16 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.13
* Thu Aug 16 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.12
* Fri Aug 10 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.11
- Fix tar archive creation for windows platfrom
* Tue Aug 07 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.10
- Fix download of public link and mtime info on listing folders
* Mon Aug 06 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.9
* Mon Aug 06 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.8
* Mon Aug 06 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.7
* Sun Aug 05 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.6
* Fri Aug 03 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.5
- Add share cache
* Thu Aug 02 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.4
- Add SWAN support
* Thu Aug 02 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.3
* Tue Jul 31 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.2
- Sharing, Favourites and Project Space support
* Tue Jul 03 2018 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.1
- First version
