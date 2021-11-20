import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    file = pd.read_csv(sys.argv[1])
    i = 0
    for subject in file.columns:
        if i != 1 and (i < 6 or subject == "Arithmancy" or subject == "Potions" or subject == "Care of Magical Creatures"):
            del file[subject]
        i += 1
    sns.pairplot(file, hue='Hogwarts House', height=1.5)
    plt.show()