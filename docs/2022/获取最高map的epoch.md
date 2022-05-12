---
title: 获取最高map的epoch
date: 2022-05-12 12:26:17
permalink: /pages/56e3ca/
categories:
  - 2022
tags:
  - 
author: 
  name: Shanya
  link: https://github.com/shanyaliux
---
# mmdetection 获取最高map的epoch

自动从训练结果中获取最高的mAP所对应的epoch。

```python
import json
import os

'''
:param work_dir 训练结果目录
:return 最好的map对应的epoch路径
'''
def getBestEpoch(work_dir):
    global maxEpoch
    fileList = os.listdir(work_dir)
    for file in fileList:
        if os.path.splitext(file)[1] == '.json':
            print(file)
            json_file = open(os.path.join(work_dir, file))
            max_mAP = 0
            for line in json_file.readlines():
                json_data = json.loads(line)
                try:
                    if json_data['mode'] == 'val':
                        if float(json_data['bbox_mAP_50']) > max_mAP:
                            max_mAP = float(json_data['bbox_mAP_50'])
                            maxEpoch = json_data['epoch']
                except:
                    pass
    return os.path.join(work_dir, 'epoch_%d.pth' % maxEpoch)

```

