import numpy as np
import matplotlib.pyplot as plt
import cv2

#%matplotlib inline

#reading the image
image = cv2.imread('C:\\Users\\ABDUL\\Pictures\\game.jpg', 1)

#converting image to size (70,50,3)
smaller_image = cv2.resize(image,(1100,1100))

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#converting image to Gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#plotting the image

cv2.imshow("legend", smaller_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

#saving image
cv2.imwrite('test_write.jpg', image)
