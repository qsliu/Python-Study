
import numpy as np

""" calculate the distance between inX and each of the samples in trainDataSet"""
def distance(inX, trainDataSet, distMethod):
    ## calcualte the distance between two samples
    trainDataSetSize = trainDataSet.shape[0]
    if distMethod == 'Euclidean':
        ## use Eucilidean distance: 2-norm of matrix
        diffMat = np.tile(inX, (trainDataSetSize, 1)) - trainDataSet
        """
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances ** 0.5
        """
        distances = np.linalg.norm(diffMat, 2,
                                   axis=1)  ## or np.linalg.norm(diffMat, 'fro', axis=1)  or np.linalg.norm(diffMat, axis=1)

    if distMethod == 'Manhattan':
        ## Manhattan distance: 1-norm
        diffMat = np.tile(inX, (trainDataSetSize, 1)) - trainDataSet
        distances = np.linalg.norm(diffMat, 1, axis=1)

    if distMethod == "Inf":
        ## infinity distance is ued:  infinity-norm
        ## Chebyshev distance or Chessboard distance
        diffMat = np.tile(inX, (trainDataSetSize, 1)) - trainDataSet
        distances = np.linalg.norm(diffMat, np.inf, axis=1)

    if distMethod == 'Cosine':
        ## calculate the Cosine similary between inX and each sample in trainDataSet
        ## Cosine similarity is particularly used in positive space, where the outcome is neatly bounded in [0,1].
        ## Cosine similarity is very efficient to evaluate, especially for sparse vectors.
        cosine_numerator = np.linalg.norm(trainDataSet * inX, axis=1)
        trainDataSet_norm2 = np.linalg.norm(trainDataSet, axis=1)
        inX_norm2 = np.linalg.norm(inX)
        distances = cosine_numerator / (trainDataSet_norm2 * inX_norm2)

    if distMethod == 'Jaccard':
        ## calculate Jaccard Similarity
        distances = np.zeros(trainDataSetSize)
        for i in range(trainDataSetSize):
            distances[i] = self.jaccardSimilarity(inX, trainDataSet[i])

    return distances


def jaccardSimilarity(self, setX, setY):
    intersectXY = set.intersection(*[set(setX), set(setY)])
    unionXY = set.union(*[set(setX), set(setY)])
    return len(intersectXY) / len(unionXY)