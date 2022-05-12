import os
import shutil


vdoingPath = r'docs'
destPath = r'rt'
vdoingList = os.listdir(vdoingPath)

indexList = []
for v in vdoingList:
    if v == '.vuepress' or v == 'index.md' or  v == '@pages':
        continue
    vp = os.path.join(vdoingPath, v)
    if os.path.isdir(vp):
        tl = os.listdir(vp)
        for t in tl:
            tp = os.path.join(vp, t)
            indexList.append(tp)
    elif os.path.isfile(vp):
        indexList.append(vp)

for i in indexList:
    file = i.split(os.sep)[-1]
    shutil.copy(i, os.path.join('./rtfd/docs', file))