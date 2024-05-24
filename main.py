from pepeline import read, save
from src.lens import lens_blur
import cv2

img = read("test/raw/1.png", 1, 0)
lens_img = lens_blur(img, 2.4)
save(lens_img, f"test/blur/lens.png")
gauss_img = cv2.GaussianBlur(img, [5, 5], 0)
save(gauss_img, f"test/blur/gauss.png")
