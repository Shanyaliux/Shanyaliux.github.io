
echo 'shanyaliux.cn' > CNAME

python utils/autoFrontmatter.py

@REM ssh root@shanyaliux.cn chattr -i /www/wwwroot/blog/docs/.vuepress/dist/.user.ini
@REM ssh root@shanyaliux.cn rm -rf /www/wwwroot/blog/*
@REM scp -r -C ./* root@shanyaliux.cn:/www/wwwroot/blog
@REM ssh root@shanyaliux.cn bash deployBlog.sh

git add .
git commit -m "push"
git push

