from typing import Union, Any
import cv2

image = cv2.imread("flower.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (41, 41), 0)
inverted_blurred: Union[int, Any] = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of flower", pencil_sketch)
cv2.waitKey(0)

