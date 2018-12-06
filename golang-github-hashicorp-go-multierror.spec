# http://github.com/hashicorp/go-multierror

%global goipath         github.com/hashicorp/go-multierror
%global commit          d30f09973e19c1dfcd120b2d9c4f168e68d6b5d5


%gometa -i

Name:           golang-github-hashicorp-go-multierror
Version:        0
Release:        0.16%{?dist}
Summary:        Package for representing a list of errors as a single error
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/hashicorp/errwrap)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.gitd30f099
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.20151116gitd30f099
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitd30f099
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitd30f099
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitd30f099
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitd30f099
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.gitd30f099
- Polish the spec file
  related: #1250466

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitd30f099
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitd30f099
- https://fedoraproject.org/wiki/Changes/golang1.6

* Tue Feb 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.6.gitd30f099
- Add missing [B]R
  related: #1250466

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitd30f099
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.gitd30f099
- Bump to upstream d30f09973e19c1dfcd120b2d9c4f168e68d6b5d5
  related: #1250466

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitfcdddc3
- Update to spec-2.1
  related: #1250466

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitfcdddc3
- Update spec file to spec-2.0
  resolves: #1250466

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitfcdddc3
- First package for Fedora
  resolves: #1212049

