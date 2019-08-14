import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pandas as pd
import random
from sklearn.neighbors import KNeighborsClassifier

print('Loading training set...')
train = pd.read_csv('datasets/clean/mnist-train.csv')
print('Loading test set...')
test = pd.read_csv('datasets/clean/mnist-test.csv')
print('Data loaded.')
knc = KNeighborsClassifier()

def plot_rand_img():
    img_i = random.randint(0, len(train)-1)

    # remove first and last columns
    im_vals = train.iloc[img_i]
    numb = im_vals.labels
    img = im_vals.values[1:-1].reshape((28, 28))

    plt.imshow(img)
    plt.title(f'Number is {numb}')
    plt.show()

def train_knc(data, labels):
    print('Fitting model...')
    knc.fit(data, labels)
    print('Model fit.')

if __name__ == '__main__':
    # plot_rand_img()
    labels = train.labels
    train_clean = train.drop(columns=['Unnamed: 0', 'labels'])
    train_knc(train_clean, labels)

    test_labels = test.labels
    test_clean = test.drop(columns=['Unnamed: 0', 'labels'])
    print('Running against test data...')
    score = knc.score(test_clean.values, test_labels.values)
    print(f'Model has {score} success rate.')
