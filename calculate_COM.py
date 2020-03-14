#Imports
import numpy as np
from scipy import ndimage

#CALCULATION OF CENTER OF MASS
def calculate_COM(matrix, N):
    '''
    Calculating center of given projections.
    param 1 (matrix, list/array): the matrix with the projections, each row is a coordinate. 
    param 2 (N, integer): the number of documents in each subfolder.
    '''
    if N == 1:
        centerofmasses = np.asarray(matrix)
        return centerofmasses

    #Splitting points for each party (documents)
    points = np.asarray(matrix)
    points = np.transpose(points)
    splits = np.split(points, int(np.shape(matrix)[1] / N), axis=0)

    #Center of masses as the mean of each party
    centerofmasses = np.mean(splits, axis=1)

    return centerofmasses
