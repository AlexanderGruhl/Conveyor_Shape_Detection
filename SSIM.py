from skimage.metrics import structural_similarity
import cv2

# Load images as grayscale
image1 = cv2.imread(r"test_image6.png", 0)
image2 = cv2.imread(r"retest_image5.png", 0)
# image3 = cv2.imread(r"test_image_2.png", 0)

# Compute SSIM between the two images
(score1, diff1) = structural_similarity(image1, image2, full=True)
# (score2, diff2) = structural_similarity(image1, image3, full=True)


# The diff image contains the actual image differences between the two images
# and is represented as a floating point data type in the range [0,1] 
# so we must convert the array to 8-bit unsigned integers in the range
# [0,255] image1 we can use it with OpenCV
diff1 = (diff1 * 255).astype("uint8")
# diff2 = (diff2 * 255).astype("uint8")
print("Image Similarity: {:.4f}%".format(score1 * 100))
# print("Image Similarity: {:.4f}%".format(score2 * 100))

cv2.imshow('diff1', diff1)
# cv2.imshow('diff2', diff2)
cv2.waitKey()