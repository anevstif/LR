import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

if __name__ == '__main__':
    file = pd.read_csv(sys.argv[1])
    i = 0
    for subject in file.columns:
        if i != 1 and (i < 6 or subject == "Transfiguration" or subject == "Charms" or subject == "Ancient Runes" or subject == "Muggle Studies" or subject == "Astronomy" or subject == "Arithmancy" or subject == "Potions" or subject == "Care of Magical Creatures"):
            del file[subject]
        i += 1
    for col in file.columns:
        sns.scatterplot(file.index, file[col])
        plt.show()
    #plt.show()
