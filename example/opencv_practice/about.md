# Opencvのインストール

```bash
pip install opencv-python
```
画像表示用で、matplotlibが便利
```bash
pip install matplotlib
```

# サンプルコードのかんたんな説明

```python
import cv2
import matplotlib.pyplot as plt

# open cvでは、デフォルトで画像がBGRで読み込まれる(なぜ...)
im = cv2.imread("fig/olivine.png")
# BGR -> RGBに変換
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
# RGB -> グレースケールに変換
im_gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
# RGB -> グレースケール画像
plt.imshow(im_gray)
plt.show()
# 暗い鉱物だけ抜き出す
plt.imshow(im_gray < 10)
plt.show()
```