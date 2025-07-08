# %%
import cv2
import matplotlib.pyplot as plt

im = cv2.imread("fig/olivine.png")

im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

im_gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

r, g, b = cv2.split(im)

plt.imshow(im_gray)
plt.show()
