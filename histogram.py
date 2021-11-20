from numpy import NaN
import pandas as pd
import sys
import matplotlib.pyplot as plt

def repart_data_from_houses(data_Hogwarts_houses, data, feature):
    i = 0
    notes_Hogwarts_houses = {
        "Gryffindor":[],
        "Ravenclaw":[],
        "Hufflepuff":[],
        "Slytherin":[],
    }
    for line in data_Hogwarts_houses:
        if line == "Gryffindor":
            notes_Hogwarts_houses['Gryffindor'].append(data[feature][i])
        elif line == "Ravenclaw":
            notes_Hogwarts_houses['Ravenclaw'].append(data[feature][i])
        elif line == "Hufflepuff":
            notes_Hogwarts_houses['Hufflepuff'].append(data[feature][i])
        elif line == "Slytherin":
            notes_Hogwarts_houses['Slytherin'].append(data[feature][i])
        i += 1
    plt.hist([notes_Hogwarts_houses['Gryffindor'], notes_Hogwarts_houses['Ravenclaw'], notes_Hogwarts_houses['Hufflepuff'], notes_Hogwarts_houses['Slytherin']], alpha = 0.5, color = ['pink', 'black', 'yellow', 'green'], label=['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin'], histtype = 'barstacked')
    plt.legend()
    plt.xlabel("Диаграмма распределения")
    plt.ylabel("Количество")
    plt.title(feature)
    plt.show()
 
if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    data_Hogwarts_houses = {}
    count = 0
    i = 0
    for features in test.columns:
        if i >= 6:
            data_Hogwarts_houses = repart_data_from_houses(test['Hogwarts House'], test, features)
        i += 1
    df = pd.DataFrame(test)
    plt.show()