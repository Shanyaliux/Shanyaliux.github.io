import os

from random import *
import time


vdoingPath = r'docs'
vdoingList = os.listdir(vdoingPath)
indexList = []
for v in vdoingList:
    if v == '.vuepress' or v == 'index.md' or  v == '@pages' or v == 'friends.md':
        continue
    vp = os.path.join(vdoingPath, v)
    if os.path.isdir(vp):
        tl = os.listdir(vp)
        for t in tl:
            tp = os.path.join(vp, t)
            indexList.append(tp)
    elif os.path.isfile(vp):
        indexList.append(vp)

permalinks = []
for i in indexList:
    file_data = ""
    with open(i, 'r', encoding="utf-8") as f:
        for line in f:
            file_data += line
        startIndex = file_data.find('---')
        if file_data[startIndex + 4: startIndex + 9] == 'title':
            endIndex = file_data[3:].find('---')
            frontMatter = file_data[:endIndex+6]
            permalinkIndex = frontMatter.find('permalink')
            categoriesIndex = frontMatter.find('categories')
            permalinks.append(frontMatter[permalinkIndex:categoriesIndex].strip('/\n').split('/')[-1])

for i in indexList:
    file = i.split(os.sep)[-1]
    file_data = ''
    with open(i, 'r+') as f:
        for line in f:
            file_data += line
        startIndex = file_data.find('---')
        if startIndex == -1 or file_data[startIndex + 4: startIndex + 9] != 'title':
            title = file.split('.')[-2]
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            permalink = "".join([choice("0123456789abcdef") for i in range(6)])
            if permalink in permalinks:
                permalink = "".join([choice("0123456789abcdef") for i in range(6)])
            frontMatter = "---\ntitle: {title}\ndate: {date}\npermalink: {permalink}\ncategories:\n  - essay\ntags:\n " \
                          " - \nauthor: \n  name: Shanya\n  link: https://github.com/shanyaliux\n---\n"\
                .format(title=title, date=date, permalink=permalink)
            f.seek(0, 0)
            f.write(frontMatter + file_data)