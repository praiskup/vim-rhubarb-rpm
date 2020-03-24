%global gitrevision 5130596a65330a4e8523d3ac1582f6c31ea6bc63
%global gitrev %(full=%gitrevision ; echo ${full:0:6} )
%global posttag git%{gitrev}
%global snapshot %{version}-%{posttag}

Name: vim-rhubarb
Version: 0
Release: 1.%{posttag}%{?dist}
Summary: GitHub support for vim-fugitive plugin
License: Vim
BuildArch: noarch

URL: https://github.com/tpope/vim-rhubarb
Source0: https://github.com/tpope/%name/archive/%gitrevision/%name-%gitrevision.tar.gz

Requires: vim-common
Requires: vim-fugitive

BuildRequires: vim-filesystem


%description
GitHub support for vim-fugitive plugin.  Enables :Gbrowse from fugitive.vim to
open GitHub URLs.  Sets up :Git to use hub if installed rather than git (when
available).  In commit messages, GitHub issues, issue URLs, and collaborators
can be omni-completed (<C-X><C-O>, see :help compl-omni).


%prep
%autosetup -p1 -n %name-%gitrevision


%install
mkdir -p %{buildroot}%{vimfiles_root}/autoload
mkdir -p %{buildroot}%{vimfiles_root}/plugin

install -D -p -m 0644 plugin/rhubarb.vim %{buildroot}%{vimfiles_root}/plugin
install -D -p -m 0644 autoload/rhubarb.vim %{buildroot}%{vimfiles_root}/autoload


%files
# license file requested: https://github.com/tpope/vim-rhubarb/issues/55
%doc doc/rhubarb.txt
%{vimfiles_root}/plugin/rhubarb.vim
%{vimfiles_root}/autoload/rhubarb.vim


%changelog
* Tue Mar 24 2020 Pavel Raiskup <praiskup@redhat.com> - 0-1.git513059
- initial packaging

