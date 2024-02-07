# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-internetarchive
Epoch: 100
Version: 3.6.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python interface to archive.org
License: AGPL-3.0-or-later
URL: https://github.com/jjjake/internetarchive/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package installs a command-line tool named ia for using Archive.org
from the command-line. It also installs the internetarchive Python
module for programmatic access to archive.org. Please report all bugs
and issues on Github.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-internetarchive
Summary: Python interface to archive.org
Requires: python3
Requires: python3-docopt >= 0.6.0
Requires: python3-jsonpatch >= 0.4
Requires: python3-requests >= 2.25.0
Requires: python3-schema >= 0.4.0
Requires: python3-tqdm >= 4.0.0
Requires: python3-urllib3 >= 1.26.0
Provides: python3-internetarchive = %{epoch}:%{version}-%{release}
Provides: python3dist(internetarchive) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-internetarchive = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(internetarchive) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-internetarchive = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(internetarchive) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-internetarchive
This package installs a command-line tool named ia for using Archive.org
from the command-line. It also installs the internetarchive Python
module for programmatic access to archive.org. Please report all bugs
and issues on Github.

%files -n python%{python3_version_nodots}-internetarchive
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-internetarchive
Summary: Python interface to archive.org
Requires: python3
Requires: python3-docopt >= 0.6.0
Requires: python3-jsonpatch >= 0.4
Requires: python3-requests >= 2.25.0
Requires: python3-schema >= 0.4.0
Requires: python3-tqdm >= 4.0.0
Requires: python3-urllib3 >= 1.26.0
Provides: python3-internetarchive = %{epoch}:%{version}-%{release}
Provides: python3dist(internetarchive) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-internetarchive = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(internetarchive) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-internetarchive = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(internetarchive) = %{epoch}:%{version}-%{release}

%description -n python3-internetarchive
This package installs a command-line tool named ia for using Archive.org
from the command-line. It also installs the internetarchive Python
module for programmatic access to archive.org. Please report all bugs
and issues on Github.

%files -n python3-internetarchive
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-internetarchive
Summary: Python interface to archive.org
Requires: python3
Requires: python3-docopt >= 0.6.0
Requires: python3-jsonpatch >= 0.4
Requires: python3-requests >= 2.25.0
Requires: python3-schema >= 0.4.0
Requires: python3-tqdm >= 4.0.0
Requires: python3-urllib3 >= 1.26.0
Provides: python3-internetarchive = %{epoch}:%{version}-%{release}
Provides: python3dist(internetarchive) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-internetarchive = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(internetarchive) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-internetarchive = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(internetarchive) = %{epoch}:%{version}-%{release}

%description -n python3-internetarchive
This package installs a command-line tool named ia for using Archive.org
from the command-line. It also installs the internetarchive Python
module for programmatic access to archive.org. Please report all bugs
and issues on Github.

%files -n python3-internetarchive
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
