import cv2
import numpy as np

# load image
img = cv2.imread(r"C:\Users\AlexG\OneDrive\Documents\OpenCV_Python\Cardboard Boxes.jpg")

# get color bounds of white region
lower =(180,180,180) # lower bound for each channel
upper = (255,255,255) # upper bound for each channel

# threshold
threshold = cv2.inRange(img, lower, upper)

# get the largest contour
contours = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
big_contour = max(contours, key=cv2.contourArea)

# get bounding box
x,y,w,h = cv2.boundingRect(big_contour)
print(x,y,w,h)


# crop the image at the bounds
crop = img[y:y+h, x:x+w]

# write result to disk
cv2.imwrite("screen_threshold.jpg", threshold)
cv2.imwrite("screen_cropped.jpg", crop)

# display it
cv2.imshow("threshold", threshold)
cv2.imshow("crop", crop)
cv2.waitKey(0)