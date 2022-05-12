#!/usr/bin/env sh

# 确保脚本抛出遇到的错误
set -e

# deploy to github pages
echo 'shanyaliux.cn' > CNAME

python autoFrontmatter.py
python vdoing2rtfd.py

git add .
git commit -m "push"
git push

