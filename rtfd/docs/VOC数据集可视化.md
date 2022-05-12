# VOC数据集可视化

```python
from gettext import find
import os
from xml.etree import ElementTree as ET
import cv2


def drawBoxOnVOC(img, xml, out, label=False):

    per=ET.parse(xml)
    image = cv2.imread(img)
    imgName = img.split('/')[-1]
    root = per.getroot()

    p=root.findall('object')

    for oneper in p:
        # print(oneper.find('name').text)
        bndbox = oneper.find('bndbox')
        x1 = (int)(bndbox.find('xmin').text)
        y1 = (int)(bndbox.find('ymin').text)
        x2 = (int)(bndbox.find('xmax').text)
        y2 = (int)(bndbox.find('ymax').text)
        # 各参数依次是：图片，添加的文字，左上角坐标(整数)，字体，字体大小，颜色，字体粗细
        # cv2.putText(img, oneper.find('name').text, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
    cv2.imwrite(os.path.join(out, imgName), image)

rootPath = 'data/images'
imgList = os.listdir(rootPath)
for imgName in imgList:
    print(imgName)
    (name, ex) = os.path.splitext(imgName)
    img = os.path.join(rootPath, imgName)
    xml = os.path.join('data/xml', name + '.xml')
    drawBoxOnVOC(img, xml, 'dataOut')
```

