import cv2, numpy as np
from pdf2image import convert_from_path

images_PIL = convert_from_path('test.pdf')
images = np.array([np.array(image) for image in images_PIL])
h, w = images[0].shape[:2]

colored = []
grayscale = []
for i, image in enumerate(images):
    image = cv2.resize(image, (w//3, h//3))
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    mask = cv2.inRange(hls, (0, 100, 100), (180, 255, 255))
    sum_mask = np.sum(mask)
    if sum_mask > 1000: colored.append(i)
    else: grayscale.append(i)

print(f'colored: {colored}')
print(f'grayscale: {grayscale}')