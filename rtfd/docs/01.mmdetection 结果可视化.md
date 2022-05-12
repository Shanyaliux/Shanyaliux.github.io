> 将此代码放入mmdetection的根目录下执行，替换相应的路径即可

```
import os

from mmdet.apis import init_detector, inference_detector

config_file = '/home/lgh/Desktop/ours/config.py'
checkpoint_file = '/home/lgh/Desktop/ours/best.pth'
device = 'cuda:0'
model = init_detector(config_file, checkpoint_file, device=device)
imgPath = '/home/lgh/code/mmdetection/data/NEU_DET/coco/train2017'
imgList = os.listdir(imgPath)
outPath = '/home/lgh/code/mmdetection/data/NEU_DET/coco/out'
if not os.path.exists(outPath):
    os.mkdir(outPath)
for img in imgList:
    image = os.path.join(imgPath,img)
    model.show_result(
        image,
        inference_detector(model, image),
        score_thr=0.3,
        show=False,
        wait_time=0,
        win_name="result",
        bbox_color=(255, 0, 0),
        text_color=(200, 200, 200),
        mask_color=None,
        out_file=os.path.join(outPath, img))

```