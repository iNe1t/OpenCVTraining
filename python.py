import cv2


img = cv2.imread('pikcha.jpg')
img2 = cv2.imread('pikcha2.jpg')
width = int(img.shape[1])
height = int(img.shape[0])
print(width)
print(height)
img = img[180:410, 0:1152]

cv2.rectangle(img2, (0, 180), (1150, 450), (0, 0, 255), 10)

# cv2.imshow("Picture", img)
cv2.imshow("Picture wuth rectangle", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
