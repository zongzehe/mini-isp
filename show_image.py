import cv2
img = cv2.imread('images/test.jpg')
cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
