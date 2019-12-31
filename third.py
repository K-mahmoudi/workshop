import os
import cv2
from matplotlib import pyplot as plt
S=64

directory = os.listdir("/content/directory to extract/Convolutional_Neural_Networks/dataset/test_set/dogs")
print(directory[16])

imgDog = cv2.imread("/content/directory to extract/Convolutional_Neural_Networks/dataset/test_set/dogs/" + directory[16])
plt.imshow(imgDog)

imgDog = cv2.resize(imgDog, (S,S))
imgDog = imgDog.reshape(1,S,S,3)

pred = classifier.predict(imgDog)
print("Probability that it is a Dog = ", "%.2f" % pred)
