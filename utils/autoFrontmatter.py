import os
import re
import random
import time
import glob

# 作者名及主页链接
AUTHOR = 'Shanya'
LINK = 'https://github.com/shanyaliux'


# 判断一个字符串是否为数字
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


# 生成一个新的permalink
def getNewPermalink():
    return hex(random.randint(1118481, 16777215))


# 得到所有的已有的permalink
def getExistsPermalinks(docsList):
    permalinks = []
    for doc in docsList:
        fileName = doc.split(os.sep)[-1]

        if not isNumber(fileName.split('.')[0]) or fileName.split('.')[1] == 'friends':
            continue

        with open(doc, encoding="utf-8", errors='ignore') as f:

            content = f.read()
            result = re.finditer(r'---+', content)
            positions = []

            for i in result:
                positions.append(i.span())

            if len(positions) < 2:
                continue

            frontMatter = content[positions[0][1]: positions[1][0]]
            permalinkSpan = re.search(r'permalink', frontMatter).span()
            categoriesSpan = re.search(r'categories', frontMatter).span()
            permalink = frontMatter[permalinkSpan[1] + 1: categoriesSpan[0] - 1]
            permalink = permalink.strip('/').split('/')[-1]
            permalinks.append(permalink)
    return permalinks


# 生成新的FrontMatter
def getFrontMatter(title, ct, permalink):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    if ct == 'posts':
        ct = 'essay'

    frontMatter = '---\n'
    frontMatter += 'title: {}\n'.format(title)
    frontMatter += 'date: {}\n'.format(date)
    frontMatter += 'permalink: /pages/{}/\n'.format(permalink)
    frontMatter += 'categories: \n - {}\n'.format(ct)
    frontMatter += 'tags: \n - {}\n'.format(ct)
    frontMatter += 'author: \n name: {}\n link: {}\n'.format(AUTHOR, LINK)
    frontMatter += '---\n\n'

    return frontMatter


if __name__=="__main__":

    docsPath = r'docs'
    docsList = glob.glob(docsPath + '/**/*.md', recursive=True)

    permalinks = getExistsPermalinks(docsList)

    for doc in docsList:
        fileName = doc.split(os.sep)[-1]

        if not isNumber(fileName.split('.')[0]) or fileName.split('.')[1] == 'friends':
            continue

        print(doc)

        with open(doc, 'r+', encoding="utf-8", errors='ignore') as f:

            content = f.read()
            result = re.finditer(r'---+', content)
            positions = []

            for i in result:
                positions.append(i.span())

            print(positions)

            if len(positions) < 2:

                print(doc)

                ct = doc.split(os.sep)[1].split('.')[1]
                title = fileName.split('.')[1]
                permalink = getNewPermalink()
                while permalink in permalinks:
                    permalink = getNewPermalink()
                frontMatter = getFrontMatter(title, ct, permalink)
                f.seek(0, 0)
                f.write(frontMatter + content)
    
    print('done!')

        

