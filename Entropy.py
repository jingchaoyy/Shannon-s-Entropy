from math import log

def calcShannonEnt(dataSet):
    countDataSet = len(dataSet)
    typeCounts={}
    for restaurant in dataSet:
        currentLabel=restaurant[-1]
        if currentLabel not in typeCounts.keys():
            typeCounts[currentLabel] = 0
        typeCounts[currentLabel] += 1

    print typeCounts

    shannonEnt = 0.0

    for type in typeCounts:
        prob = float(typeCounts[type])/countDataSet
        shannonEnt -= prob * log(prob,2)


    return shannonEnt


dataSet1 = [['Chinese'], ['Chinese'], ['Japan'], ['Chinese'], ['Japan']]
dataSet2 = [['Chinese'], ['Italian'], ['Japan'], ['Chinese'], ['Japan']]

print calcShannonEnt(dataSet1)
print calcShannonEnt(dataSet2)
