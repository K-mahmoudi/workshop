directory = os.listdir("/content/directory to extract/Convolutional_Neural_Networks/dataset/test_set/cats")
print(directory[10])

imgCat = cv2.imread("/content/directory to extract/Convolutional_Neural_Networks/dataset/test_set/cats/" + directory[15])
plt.imshow(imgCat)

imgCat = cv2.resize(imgCat, (S,S))
imgCat = imgCat.reshape(1,S,S,3)

pred = classifier.predict(imgCat)
print("Probability that it is a Cat = ", "%.2f" % (1-pred))
