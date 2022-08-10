#!/usr/bin/env sh

yarn install
yarn build
cp -r /www/wwwroot/Shanyaliux.github.io/docs/.vuepress/dist/* /www/wwwroot/blog/