import cv2
import matplotlib.pyplot as plt
 
image=cv2.imread("flower.jpg")

#BGR TO RGB
imagergb=cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
plt.imshow(imagergb)
plt.title("RGB image")
plt.show()

#BGR TO GREYSCALE
imagegrey=cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
plt.imshow(imagegrey)
plt.title("GRAY image")
plt.show()

#Cropping the image
crop_image=image[500:1750 , 500:2300]
crop_image=cv2.cvtColor(crop_image,cv2.COLOR_BGR2RGB)
plt.imshow(crop_image)
plt.title("Crop region")
plt.show()

(h,w)=image.shape[:2]
center=(w//2 , h//2)
m=cv2.getRotationMatrix2D(center,45,1.0)
rotate=cv2.warpAffine(image,m,(w,h))
rotatergb=cv2.cvtColor(rotate , cv2.COLOR_BGR2RGB)
plt.imshow(rotatergb)
plt.title("Rotated Image")
plt.show()



# rotate by 45 degrees

# Increase brightness by adding 50 to all pixel values

brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()
