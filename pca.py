import numpy as np

def eigendecompose(X):
    ''' Return the eigendecomposition (E, V) of X s.t. eigenvalues are sorted descendingly '''
    lam, V = np.linalg.eigh(X)
    sort_idx = np.argsort(lam)[::-1]
    return lam[sort_idx], V[:, sort_idx]

def PCA_zdoc(A,k=3):
    B = np.matmul(A, A.T)
    C = np.matmul(A.T, A)

    lambdas, V = eigendecompose(C)
    lambdas, U = eigendecompose(B)

    Uk = U[:, :k]
    Sk = lambdas[:k]

    # define projection matrix for the documents
    P = np.diag(1./np.sqrt(Sk))@Uk.T
    # project
    return P@A
