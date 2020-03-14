import matplotlib.pyplot as plt
import re
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Color mapping for the parties
__party_colors = {
    'Socialdemokratiet': 'red',
    'Socialistisk Folkeparti': 'pink',
    'Venstre': 'blue',
    'Alternativet': 'green',
    'Radikale Venstre': 'purple',
    'Dansk Folkeparti': 'yellow',
    'Enhedslisten': 'orange',
    'Det Konservative Folkeparti': 'lightgreen',
    'Liberal Alliance': 'lightblue'
}

def __getColor(label):
    return __party_colors[re.sub('[0-9]','',label)]

def __plotPartyLabels(labels, doc_N):
    ax_second = plt.subplot(1, 2, 2)
    plt.axis('off')
    for i,k in enumerate(__party_colors.keys()):
        circle = plt.Circle((0.5,0.25-i/len(labels)), radius=0.010, color=__party_colors[k])
        ax_second.add_patch(circle)
        ax_second.annotate(k,xy=(0,0.25-i/len(labels)), fontsize=20)



def plotParties2D(doc_N, labels,z_doc):
    plt.figure(figsize=(25, 15))
    ax = plt.subplot(1, 2, 1)
    plt.ylim(-1,1)
    plt.xlim(-1,1)

    l = len(z_doc[0])
    xs = np.split(z_doc[0], l/doc_N)
    ys = np.split(z_doc[1], l/doc_N)

    for i in range(len(xs)):
        ax.scatter(xs[i],ys[i], c=__getColor(labels[i]))

    plt.xlabel('Latent Semantic dim 2', fontsize=18)
    plt.ylabel('Latent Semantic dim 3', fontsize=18)
 
    __plotPartyLabels(labels, doc_N)
 
    plt.show()

def plotParties3D(doc_N, labels, z_doc):
    '''
    documents: all documents
    doc_N: the number of documents for each party
    labels: names of the parties, index matching documents
    z_doc: the projection of the documents into new basis
    '''
    plt.ylim(-1,1)
    plt.xlim(-1,1)
    parties = list(__party_colors.keys())
    fig = plt.figure(figsize=(25,15))
    ax = fig.add_subplot(1,2,1, projection='3d')

    l = len(z_doc[0])
    xs = np.split(z_doc[0], l/doc_N)
    ys = np.split(z_doc[1], l/doc_N)
    zs = np.split(z_doc[2], l/doc_N)

    for i in range(len(xs)):
        ax.scatter(xs[i],ys[i],zs[i], c=__getColor(parties[i]))
    
    ax.set_xlabel('Second Principale Component')
    ax.set_zlabel('Third Principale Component')
    ax.set_ylabel('Fourth Principale Component')

    __plotPartyLabels(labels, doc_N)

    plt.show()


def plotPartiesTerms(vocabulary, labels, z_doc, z_word):
    vocab_size = len(vocabulary)

    plt.figure(figsize=(25, 15))
    ax = plt.subplot(1, 2, 1)
    plt.ylim(-1,1)
    plt.xlim(-1,1)

    for idx, doc in enumerate(z_doc.T):
        circle = plt.Circle((doc[0], doc[1]), radius=0.010, color=__getColor(labels[idx]))
        ax.add_patch(circle)
        label = ax.annotate('',xy=(doc[0], doc[1]), fontsize=20, ha="center", va="center")

    plt.xlabel('Latent Semantic dim 1', fontsize=18)
    plt.ylabel('Latent Semantic dim 2', fontsize=18)
 
    for idx, term in enumerate(z_word):
        circle = plt.Circle((term[0], term[1]), radius=0.010, color='r')
        ax.add_patch(circle)
        label = ax.annotate(idx, xy=(term[0], term[1]), fontsize=20, ha="center", va="center")
 
    plt.xlabel('Latent Semantic dim 1')
    plt.ylabel('Latent Semantic dim 2')
 
    ax_second = plt.subplot(1, 2, 2)
    plt.axis('off')
    for idx, term in enumerate(vocabulary):
        i = idx
        plt.text(0.85, 1 - i/vocab_size, 'Term %d: %s' % (i, term), color='r')

    __plotPartyLabels(labels)

    plt.show()
