## COCO数据集可视化
```python
import json
import os

import cv2


class CocoDataVisualization:
    def __init__(self, imgPath, jsonPath):
        self.imgPath = imgPath
        self.jsonPath = jsonPath

    def visualize(self, out, color=(0, 255, 255), thickness=1):
        with open(self.jsonPath, 'r') as f:
            annotation_json = json.load(f)

        for img in annotation_json['images']:
            image_name = img['file_name']  # 读取图片名
            id = img['id']  # 读取图片id
            image_path = os.path.join(self.imgPath, str(image_name).zfill(5))  # 拼接图像路径
            image = cv2.imread(image_path, 1)  # 保持原始格式的方式读取图像
            num_bbox = 0  # 统计一幅图片中bbox的数量

            for i in range(len(annotation_json['annotations'][::])):
                if annotation_json['annotations'][i - 1]['image_id'] == id:
                    num_bbox = num_bbox + 1
                    x, y, w, h = annotation_json['annotations'][i - 1]['bbox']  # 读取边框
                    image = cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), color=color,
                                          thickness=thickness)
            cv2.imwrite(os.path.join(out, image_name), image)


if __name__ == '__main__':
    # the first param is the directory's path of images
    # the second param is the path of json file
    d = CocoDataVisualization('/home/lgh/code/mmdetection/data/NEU_DET/coco/train2017',
                              '/home/lgh/code/mmdetection/data/NEU_DET/coco/annotations/instances_train2017.json')

    # this param is the output path
    d.visualize('./out')

```



## VOC数据集可视化

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

