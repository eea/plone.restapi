#!/bin/sh

set -x

git remote add upstream https://github.com/plone/plone.restapi.git

git fetch --all
git pull
git merge --no-ff origin/improve_portlets
git merge --no-ff upstream/master
git merge --no-ff upstream/eea-dx-cpanel-metadata
# git merge origin/export_components
