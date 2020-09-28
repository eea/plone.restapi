#!/bin/sh

set -x

git remote add upstream https://github.com/plone/plone.restapi.git

git fetch --all
git pull
git merge origin/improve_portlets
git merge upstream/master
git merge upstream/eea-layout-endpoint

# Merged
# git merge --no-ff upstream/eea-dx-cpanel-metadata
# git merge origin/export_components
