import os

png_images = [f for f in os.listdir("results/") if f.endswith(".png")]
print(png_images)
