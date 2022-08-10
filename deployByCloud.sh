#!/usr/bin/env sh

chattr -i docs/.vuepress/dist/.user.ini
yarn install
yarn build