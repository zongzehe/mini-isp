# Mini-ISP 学习日记
大二上 16-Week 挑战：用树莓派+IMX219 完成最简单 ISP 流水线。

## Week1 进度
- [x] 环境搭建 Python3.11 + OpenCV
- [x] 能读取并显示图片
- [ ] 解析 RAW 文件（下周）

## 效果展示
![第一张测试图](file:///E:/Pictures/1/Lena.bmp.jpg)

## 脚本
```python
import cv2
img = cv2.imread('images/test.jpg')
cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
