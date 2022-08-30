import cv2

img = cv2.imread("fossilpic5.png")
img[208,182]=[255, 255, 255]
img[183,658]=[255, 255, 255]
img[755,688]=[255, 255, 255]
img[779,211]=[255, 255, 255]
cv2.imshow('title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
