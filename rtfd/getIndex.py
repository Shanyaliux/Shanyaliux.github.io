import os


def getIndex():
    title = "Welcome to Shanya's blog!\n================================\n\n"
    toctree = ".. toctree::\n   :maxdepth: 2\n   :caption: Contents\n\n"

    rootPath = "../docs"
    rootList = os.listdir(rootPath)
    indexList = []
    for r in rootList:
        if r == '.vuepress' or r == 'index.md' or r == '@pages':
            continue
        rp = os.path.join(rootPath, r)
        if os.path.isdir(rp):
            tl = os.listdir(rp)
            for t in tl:
                tp = os.path.join(rp, t)
                indexList.append(tp)
        elif os.path.isfile(rp):
            indexList.append(rp)

    indexList = sorted(indexList, key=lambda x: os.path.getmtime(x), reverse=True)
    with open('./index.rst', 'w', encoding="utf-8") as f:
        f.write(title)
        f.write(toctree)
        for i in indexList:
            f.write('   {}\n'.format(i))


if __name__ == '__main__':
    getIndex()
