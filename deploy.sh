#!/usr/bin/env sh

# 确保脚本抛出遇到的错误
set -e

# deploy to github pages
echo 'shanyaliux.cn' > CNAME

python ./rtfd/getIndex.py 

git add .
git commit -m "push"
git push

