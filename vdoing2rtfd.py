import os
from re import L
import shutil


vdoingPath = r'docs'
destPath = r'rtfd'
vdoingList = os.listdir(vdoingPath)
shutil.rmtree(os.path.join(destPath, 'docs'))  
os.mkdir(os.path.join(destPath, 'docs')) 
indexList = []
for v in vdoingList:
    if v == '.vuepress' or v == 'index.md' or  v == '@pages' or v == '99.friends.md':
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
    destFile = os.path.join('./rtfd/docs', file)
    shutil.copy(i, destFile)
    file_data = ""
    with open(destFile, 'r', encoding="utf-8") as f:
        for line in f:
            file_data += line
        startIndex = file_data.find('---')
        if file_data[startIndex + 4: startIndex + 9] == 'title':
            file_data = file_data[3:]
            endIndex = file_data.find('---')
            file_data = file_data[endIndex+4:]
    with open(destFile, "w", encoding="utf-8") as f:
        f.write(file_data)
    