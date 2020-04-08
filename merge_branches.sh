#!/bin/sh

set -x

git remote add upstream https://github.com/plone/plone.restapi.git

git fetch --all
git pull
git merge origin/improve_portlets
# git merge origin/export_components
