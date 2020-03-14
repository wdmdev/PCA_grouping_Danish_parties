# Import packages
#%matplotlib inline
import pylab as plt
import seaborn as snb
import numpy as np
import pandas as pd
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable
snb.set_style('darkgrid')
from fileLoader import loadFiles
from fileLoader import SplitType
from bag import construct_bag_of_words
from fileCleaner import remove_stop_words, load_stop_words
import pca
from nltk.stem.snowball import SnowballStemmer
from plotParties import *
from tbtdbdmatrices import *
from calculate_COM import calculate_COM
from vectorDistance import vectorDistance

# Preprocessering of document
folder = 'PolitikSammeSager'
print('Data set: {0}'.format(folder))
split_type=SplitType.Lines
print('Split setting: {0}'.format(split_type))
num_of_lines=85
if split_type == SplitType.Lines:
    print('Number of lines in splits: {0}'.format(num_of_lines))
documents,labels = loadFiles(folder, split_type, num_of_lines)
doc_N = len(documents)/len(labels)
print('Number of documents per party: {0}'.format(doc_N))
print('Number of documents: {0}'.format(len(documents)))


# split documents into words and count
stemmer = SnowballStemmer('danish')
words = ' '.join(documents).split(' ')
words = [stemmer.stem(word) for word in words]
num_words = len(words)

# Create vocabulary from preprosseced documents
def get_vocabulary(words):
    ''' This function takes a list of words and return the vocabulary. That is, a sorted list of all the words that occur at least once in the documents.'''
    vocabulary = sorted(list(set(words)))
    return vocabulary

vocabulary = get_vocabulary(words)
# remove stop words from vocabulary
stop_words = load_stop_words("stopwords.txt")
stop_words = [stemmer.stem(w) for w in stop_words]

with open('stemmed_stop_words.txt', 'a+') as stop:
    for sw in stop_words:
        stop.write('{0}\n'.format(sw))

vocabulary = remove_stop_words(vocabulary, stop_words)
# count number of words in vocabulary again
vocab_size = len(vocabulary)

# Make A the bag-of-words
A = construct_bag_of_words(documents, vocabulary)

#Projections of A into eigen vector space
k = 3
print('k = {0}'.format(k))
z_doc = pca.PCA_zdoc(A,k)

plotParties2D(doc_N, labels, z_doc[1:])
#plotParties3D(doc_N, labels, z_doc[1:]) #Only works with z > 3

#Center of mass for each party
com = calculate_COM(z_doc[1:], doc_N)

plotParties2D(1, labels, com.T)

for i in range(len(labels)):
    print('Party: {0} '.format(labels[i]))
    distances = vectorDistance(com,i)
    maxDis = np.argmax(distances)
    distances[i] = np.sum(distances) #set distance to self to large number to avoid it
    minDis = np.argmin(distances)
    print('Closest to: {0}, distance: {1}'.format(labels[minDis], distances[minDis]))
    print('Furthest from: {0}, distance: {1}'.format(labels[maxDis], distances[maxDis]))
    print('------------------------------\n')

print(labels)
for i in range(len(labels)):
    print('{0}:  {1}'.format(labels[i], vectorDistance(com,i)))
