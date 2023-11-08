from skimage.metrics import structural_similarity
import cv2

# Load images as grayscale
image1 = cv2.imread(r"C:\Users\AlexG\OneDrive\Documents\OpenCV_Python\Red Box.png", 0)
image2 = cv2.imread(r"C:\Users\AlexG\OneDrive\Documents\OpenCV_Python\Red Box Line.png", 0)

# Compute SSIM between the two images
(score, diff) = structural_similarity(image1, image2, full=True)

# The diff image contains the actual image differences between the two images
# and is represented as a floating point data type in the range [0,1] 
# so we must convert the array to 8-bit unsigned integers in the range
# [0,255] image1 we can use it with OpenCV
diff = (diff * 255).astype("uint8")
print("Image Similarity: {:.4f}%".format(score * 100))

cv2.imshow('diff', diff)
cv2.waitKey()