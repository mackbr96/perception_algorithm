import numpy as np
from numpy import linalg
normalVector = []
def train():
    with open("train.txt") as f:
        lines = f.readlines()
        vectors = []
        for i in lines:
            vectors.append(i.split())

    flags = [] #Y or N

    for i in range(0, len(vectors)): #remove flag from vector and convert string to float
        flags.append(vectors[i].pop())
        for x in range(0,len(vectors[i])):
            vectors[i][x] = float(vectors[i][x])

    #set up first normal vector
    if(flags[0] == "Y"):
        normalVector = vectors[0] / linalg.norm(vectors[0])
    else:
        normalVector = vectors[0] / linalg.norm(vectors[0])*-1

    vec = np.array(vectors)

    for i in range(0, len(vectors)):
        if(flags[i] == "Y"): #Yes side
            if(np.inner(normalVector, vec[i]) >= 0): #Is good
                continue
            else: #Its on the wrong side
                normal = vec[i] / linalg.norm(vec[i])
                normalVector= normalVector + (normal)
                i = 0
        else: #No side
            if(np.inner(normalVector, vec[i]) < 0): #Is good
                continue
            else: #Is incorrect
                normal = vec[i] / linalg.norm(vec[i])
                normalVector= normalVector + (-1 * normal)
                i = 0
    return normalVector

def test(normalVector):
    with open("test.txt") as f:
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



normalVector = train()

print(normalVector)
print("FINISHED LEARNING")
print("NOW TESTING")

predictions = test(normalVector)

print(predictions)
print("Finished")