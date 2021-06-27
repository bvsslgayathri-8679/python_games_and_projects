import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read dataset
dataset=pd.read_csv('f:/projects/test.csv').as_matrix()


# classifier

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()

X_train = dataset[0:21000,1:]
y_train = dataset[0:21000,0]

'''
X_train = dataset[:,1:]
y_train = dataset[:,0]
'''

# fitting to the dataset

classifier.fit(X_train, y_train)

# testing data

X_test = dataset[21000:,1:]
y_test = dataset[21000:,0]

'''
testdata = pd.read_csv('test.csv').as_matrix()
X_test = testdata[:,:]
y_test = dataset[:,0]
'''

# input

inp = X_test[2000]

# shape in matrix

inp.shape = (28,28)

# show the output in white background and black text-color

plt.imshow(255-inp,cmap='gray')

# print

print(classifier.predict( [X_test[2000]] ))  # can't use inp...Error : format
plt.show()

# prediction

pred = classifier.predict(X_test)

# accuracy calculation

count = 0
for i in range(0,21000):
    count += 1 if pred[i]==y_test[i] else 0
print("Accuracy =", (count / 21000) * 100)