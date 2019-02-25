## implement a knn in this file
## author : Mengmeng Liu
## date: 02/12/2019


import numpy as np
import operator
import distanceMeasure

class CreateDataSet:
    def __init__(self):
        self.dataset = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
        self.labels = ['A', 'A', 'B', 'B']



class SuperviseClassify:

    """
        inX: array type
        trainDataSet: array or matrix
        trainLabels: array
    """
    def __init__(self, inX, trainDataSet, trainLabels):
        self.inX = inX
        self.trainDataSet = trainDataSet
        self.trainLabels = trainLabels

    """
        ## use the trainDataSet and its cooresponding labels: trainLabel to determine the label of inX
        k: number of nearest neighbors  
    """
    def classifyKNN(self, k):
        ## calculate the distance between inX and each point in trainDataSet
        distances = distanceMeasure.distance(self.inX, self.trainDataSet, 'Euclidean')
        ## sort the distances in ascending order
        sortedDistance = distances.argsort()        ## sort index of each element in distances

        ## take k items with lowest distance to inX
        classCount = {}
        for i in range(k):
            voteLabel_i = self.trainLabels[sortedDistance[i]]
            classCount[voteLabel_i] = classCount.get(voteLabel_i, 0) + 1
            ## classCount.get(voteLabel_i, 0)   => get value from dictionary classCount, by its key voteLabel_i, if the key deos not exist, then return 0

        # sort the dictionary of neighbor counts (number of votes)
        sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)

        ## return the label with majority vote. its vote is: sortedClassCount[0][1]
        return sortedClassCount[0]


    def classifyDecisionTree(self):
        pass



def main():

    myTrainDataSet = CreateDataSet()

    testSample = np.array([2, 3])

    myClassifier = SuperviseClassify(testSample, myTrainDataSet.dataset, myTrainDataSet.labels)

    ## test k-NN
    k = 4
    testSampleLabel_kNN = myClassifier.classifyKNN(k)

    ## test decision tree

    print("the label of %s is %s \t with %d votes" % (str(testSample), str(testSampleLabel_kNN[0]), testSampleLabel_kNN[1]))

    x = np.array([3, 45, 7, 2])
    y = np.array([[2, 54, 13, 15], [2, 54, 13, 15]])
    print(distanceMeasure.distance(x,y, 'Cosine'))

if __name__ == "__main__":
    main()
