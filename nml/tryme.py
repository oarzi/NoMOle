import cv2

from WorkingPys.K2means import k2means

pic = 'images\malignant\m1.jpg'

res2 = k2means(pic)

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
