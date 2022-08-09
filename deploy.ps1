
# deploy to github pages
echo 'shanyaliux.cn' > CNAME

python utils/autoFrontmatter.py

ssh root@shanyaliux.cn rm -rf /root/blog/*
scp -r -C ./* root@shanyaliux.cn:/root/blog
ssh root@shanyaliux.cn bash deployBlog.sh

git add .
git commit -m "push"
git push

