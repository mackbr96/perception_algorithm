import numpy as np
from numpy import linalg

def train():
    with open("train.txt") as f:
        lines = f.readlines()
        vectors = []
        for i in lines:
            vectors.append(i.split())

    labels = [] #Y or N

    for i in range(0, len(vectors)): #remove flag from vector and convert string to float
        labels.append(vectors[i].pop())
        for x in range(0,len(vectors[i])):
            vectors[i][x] = float(vectors[i][x])

    vec = np.array(vectors)

    if(labels[0] == "Y"):
        normalVector = vec[0] / linalg.norm(vectors[0])
    else:
        normalVector = vec[0] / linalg.norm(vectors[0])*-1

    i = -1
    while(i < len(vec) - 1):
        i += 1
        if(labels[i] == "Y"): #Yes side
            if(np.inner(normalVector, vec[i]) >= 0): #Is good
                continue
            else: #Its on the wrong side
                normal = vec[i] / linalg.norm(vec[i])
                normalVector= np.add(normalVector, normal)
                i = -1
        elif(labels[i] == "N"): #No side
            if(np.inner(normalVector, vec[i]) < 0): #Is good
                continue
            else: #Is incorrect
                normal = vec[i] / linalg.norm(vec[i])
                normalVector= np.add(normalVector, (-1 * normal))
                i = -1
        else:
            continue
    return normalVector, labels


def test(normalVector):
    with open("tester.txt") as f:
        lines = f.readlines()
        vectors = []
        for i in lines:
            vectors.append(i.split())

    for i in range(0, len(vectors)): #Convert string to float in vectors
        for x in range(0,len(vectors[i])):
            vectors[i][x] = float(vectors[i][x])

    vec = np.array(vectors)

    predictions = [] #Our predictions for the test

    for i in range(0, len(vectors)): 
        if(np.inner(normalVector, vec[i]) >= 0):
            predictions.append("Y")
        else:
            predictions.append("N") 
    return predictions



normalVector,labels = train()

print(normalVector)
print("FINISHED LEARNING")
print("NOW TESTING")
wrong = 0
right = 0

predictions = test(normalVector)
for i in range(0, len(predictions)):
    if predictions[i] != labels[i]:
        wrong += 1
    else:
        right += 1

print("Right " + str(right))
print("Wrong " + str(wrong))
#print(predictions)
print("Finished")