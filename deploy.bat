
echo 'shanyaliux.cn' > CNAME

python utils/autoFrontmatter.py

ssh root@shanyaliux.cn chattr -i /www/wwwroot/blog/docs/.vuepress/dist/.user.ini
ssh root@shanyaliux.cn rm -rf /www/wwwroot/blog/*
scp -r -C ./* root@shanyaliux.cn:/www/wwwroot/blog
ssh root@shanyaliux.cn bash deployBlog.sh

git add .
git commit -m "push"
git push

