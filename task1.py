import cv2
import matplotlib.pyplot as plt
print("Program started!")
image = cv2.imread("moon.jpg")
if image is None:
   print("Image not found! Check the image filename and folder.")
else:
   print("Image loaded successfully!")  
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("FULL MOON")
plt.axis("off")
plt.show()
height, width = image.shape[:2]
print("Image Width:", width)
print("Image Height:", height)
print("Image Shape:", image.shape)
print("Image Data Type:", image.dtype)
success = cv2.imwrite("moon_copy.jpg", image)

if success:
    print("Image saved successfully!")
else:
    print("Image could not be saved!")

