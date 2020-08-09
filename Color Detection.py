
import cv2  
import numpy as np


green = np.uint8([[[0, 255, 0]]])
hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsvGreen) 

lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
upperLimit = hsvGreen[0][0][0] + 10, 255, 255

print(upperLimit)
print(lowerLimit)

red = np.uint8([[[0, 0, 255]]])
hsvred = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
print(hsvred)

lower = hsvred[0][0][0] - 10, 100, 100
upper = hsvred[0][0][0] + 10, 255, 255

print(upper)
print(lower)

image = cv2.imread(r'picture.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lg = np.array(lowerLimit)
ug = np.array(upperLimit)

green_mask = cv2.inRange(hsv, lg, ug)
cv2.imshow('green', green_mask)

lr = np.array(lower)
ur = np.array(upper)

red_mask = cv2.inRange(hsv, lr, ur)
cv2.imshow('red', red_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
