from math import nan
import numpy as np
import pandas as pd
import sys
from sklearn import impute
import csv

if __name__ == '__main__':
    baza = pd.read_csv(sys.argv[1])
    matrice = np.loadtxt("theta.txt")
    i = 0
    real_houses = baza["Hogwarts House"]
    for features in baza.columns:
        if i < 6 or features == "Arithmancy" or features == "Potions" or features == "Care of Magical Creatures":
            del baza[features]
        i += 1
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    imputer = impute.SimpleImputer(missing_values=nan,strategy="mean")
    c = imputer.fit_transform(np.array(baza))
    i = 0
    for column in c.T:
        if (matrice[:,1][i] != 0):
            c[:,i] = (column - matrice[:,0][i]) / matrice[:,1][i]
        i += 1
    M = np.c_[c, np.ones((np.size(c, 0)))]
    theta = np.delete(matrice, np.s_[0:2], 1)
    j = 0
    header = ["Index", "Hogwarts House"]
    baza = []
    for student in M:
        maximum = [0, 0, 0, 0]
        for i in range(0, 4):
            maximum[i] = float(1/(1 + np.exp(np.negative(np.dot(student, theta[:,i])))))
        baza.append([j, houses[maximum.index(max(maximum))]])
        j += 1
    with open('houses.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(baza)