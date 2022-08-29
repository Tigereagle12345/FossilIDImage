import cv2

y = 46
x = 39

img = cv2.imread("fossilpic5.png")
img[y,x]=[255, 255, 255]
img[129,129]=[255, 255, 255]
img[46,129]=[255, 255, 255]
img[129,39]=[255, 255, 255]
cv2.imshow('title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
