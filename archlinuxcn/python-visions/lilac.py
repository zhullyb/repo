#!/usr/bin/env python3

from lilaclib import *


def pre_build():
    update_pkgver_and_pkgrel(_G.newver.lstrip("v"))


def post_build():
    git_add_files("PKGBUILD")
    git_commit()
    update_aur_repo()
