# Calculate distance between mean vectors of documents 
import numpy as np
import math
from scipy.spatial import distance

def vectorDistance(M, partyNumber):

    # Define matrix that will show distances
    distanceMatrix = np.array([])
    M_len = len(M)
    M = np.transpose(M)
    # For every column calculate euclidean distance between points in n dimensions
    for i,col in enumerate(range(M_len)):
        distanceMatrix = np.insert(distanceMatrix, col, distance.euclidean(M[:,partyNumber], M[:,col]))

    return distanceMatrix
