import numpy
normalVector = []

with open("train.txt") as f:
    lines = f.readlines()
    vectors = []
    for i in lines:
        vectors.append(i.split())
        
vectors[0].pop(len(vectors[0]) - 1)
normalVector = vectors[0]
vector = 