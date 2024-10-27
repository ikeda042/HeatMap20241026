import os
import numpy as np
from PIL import Image


# 画像のサイズを調整する関数
def resize_image(image, size):
    return image.resize(size, Image.LANCZOS)


# 画像のサイズを指定（(14:9)）
target_size = (700, 450)

# PNG画像のリストを取得
png_images = [f for f in os.listdir("results/") if f.endswith(".png")]
print(png_images)

# 画像を読み込み、サイズを調整
images = [resize_image(Image.open(f"results/{f}"), target_size) for f in png_images]

# 画像を結合
n = 3
rows = len(images) // n
images = [np.hstack(images[i * n : (i + 1) * n]) for i in range(rows)]
image = np.vstack(images)
Image.fromarray(image).save("combined.png")
