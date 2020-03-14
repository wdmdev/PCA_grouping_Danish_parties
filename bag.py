import numpy as np


# Create bag of words from documents and vocabulary
def construct_bag_of_words(documents, vocabulary):
    '''
    This functions takes a list of documents and a vocabulary a returns the corresponding bag-of-words representation of the documents

    If the variable "document" is a list of N documents and the variable "vocabulary" is a list of M words, then the function should return a bag-of-words matrix A of size N x M matrix.
    If some word from a document is not present in the vocabulary, it should be ignored.
    '''
    # Find length of document and of vacabulary
    num_doc = len(documents)
    vocab_size = len(vocabulary)
    # For each word in vocabulary get index
    word2idx = {word: idx for idx, word in enumerate(vocabulary)}
    # Create empty matrix with dimensions fitted to sizes of vacabulary and document
    bag_of_words = np.zeros((vocab_size, num_doc))

    # Create matrix of bag-of-words
    for i in range(num_doc):
        tempWords = documents[i].split(" ")
        for j in range(len(tempWords)):
            if tempWords[j] in vocabulary:
                index = word2idx[tempWords[j]]
                bag_of_words[index, i] += 1
    return bag_of_words

