'''
In this document term-by-term and document-by-document matrices are calculated (B matrix is also called the co-occurence matrix). 
This is done to illustrate how certain words and documents are related to each other.
We work with three matrices. A (bag), B=A.A^T, and C=A^T.A
'''
#Imports
from bag import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def termbydocument(documents, vocabulary, A):
    '''
    This function visualizes the bag-of-words-matrix.
    '''
    #Defining necessary variables
    vocab_size = len(vocabulary)

    #Plotting 
    plt.figure(figsize=(20, 6))
    ax = plt.subplot(1, 3, 1)
    im = plt.imshow(A)
    plt.xlabel('Doc')
    plt.yticks(np.arange(0, vocab_size), vocabulary)
    plt.title('$A$ (Term x document)')
    plt.grid(False)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="15%", pad=0.1)
    plt.colorbar(im, cax=cax)

    return ''


def termbyterm(documents, vocabulary, A):
    '''
    This function visualizes the term-by-term matrix (B). Compares words to words in vocabulary.
    '''
    #Defining B
    B = np.matmul(A, A.T)

    #Plotting
    ax = plt.subplot(1, 3, 2)
    im = plt.imshow(B)
    plt.xlabel('Terms')
    plt.ylabel('Terms')
    plt.title('$B = AA^T$ (Term x Term)')
    plt.grid(False)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    plt.colorbar(im, cax=cax)

    return ''

def documentbydocument(documents, vocabulary, A):
    '''
    This function compares document to document in documents.
    '''
    #Defining C
    C = np.matmul(A.T, A)

    #Plotting
    ax = plt.subplot(1, 3, 3)
    im = plt.imshow(C)
    plt.xlabel('Doc')
    plt.ylabel('Doc')
    plt.title('$C = A^T A$ (Document x Document)')
    plt.grid(False)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    plt.colorbar(im, cax=cax)

    return ''