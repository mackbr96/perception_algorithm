import numpy as np
from numpy import linalg
normalVector = []

with open("train.txt") as f:
    lines = f.readlines()
    vectors = []
    for i in lines:
        vectors.append(i.split())

flags = []

for i in range(0, len(vectors)):
    flags.append(vectors[i].pop())
    for x in range(0,len(vectors[i])):
        vectors[i][x] = float(vectors[i][x])

#set up first normal vector
if(flags[0] == "Y"):
    normalVector = vectors[0]
else:
    normalVector = vectors[0]*-1


vec = np.array(vectors)
no = np.array(normalVector)
no = no / linalg.norm(no)

for i in range(0, len(vectors)):
    if(flags[i] == "Y"):
        if(np.inner(no, vec[i]) >= 0):
            continue
        else:
            normal = vec[i] / linalg.norm(vec[i])
            no = no + (normal)
            i = 0
    else:
        if(np.inner(no, vec[i]) < 0):
            continue
        else:
            normal = vec[i] / linalg.norm(vec[i])
            no = no + (-1 * normal)
            i = 0
print(no)
print("FINISHED LEARNING")
print("NOW TESTING")

with open("test.txt") as f:
    lines = f.readlines()
    vectors = []
    for i in lines:
        vectors.append(i.split())


for i in range(0, len(vectors) ):
    for x in range(0,len(vectors[i])):
        vectors[i][x] = float(vectors[i][x])


vec = np.array(vectors)

solution = []

for i in range(0, len(vectors)):
    if(np.inner(no, vec[i]) >= 0):
        solution.append("Y")
    else:
        solution.append("N") 


print(solution)
print("Finished")







    