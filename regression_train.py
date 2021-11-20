from Math import *
import pandas as pd
import sys
from math import nan
import numpy as np
from sklearn import preprocessing
from sklearn import impute


class Log_reg(object):
    def __init__(self, data, data_y):
        self.min_max_scaler = preprocessing.Normalizer()
        self.size_lines = np.size(data, 0)
        self.size_columns = np.size(data, 1) + 1
        self.result = np.zeros(shape=(self.size_columns, 6))
        self.X = self.get_X(data)
        self.theta = self.get_theta(self.size_columns)
        self.get_result(data_y)

    def get_result(self, data_y):
        houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
        for i in range(0, 4):
            self.theta = self.get_theta(self.size_columns)
            self.Y = self.get_Y(data_y, houses[i])
            self.gradient_descent(i)
        np.savetxt("theta.txt", self.result)

    def get_X(self, data):
        i = 0
        mean = []
        std = []
        imputer = impute.SimpleImputer(missing_values=nan, strategy="mean")
        X = imputer.fit_transform(data)
        for column in X.T:
            math = Math(column)
            X[:, i] = (column - math.mean) / math.std
            i += 1
            mean.append(math.mean)
            std.append(math.std)
        mean.append(0)
        std.append(0)
        self.result[:, 0] = np.array(mean)
        self.result[:, 1] = np.array(std)
        return np.c_[X, np.ones((self.size_lines))]

    def get_Y(self, data, present_house):
        ret = []
        for house in data:
            if house == present_house:
                ret.append(1)
            else:
                ret.append(0)
        M = np.array(ret).reshape(self.size_lines, 1)
        return M

    def get_theta(self, size):
        M = np.zeros((size, 1))
        return M

    def model(self):
        return 1 / (1 + np.exp(np.negative(np.dot(self.X, self.theta))))

    def gradient(self):
        return 1 / self.size_lines * self.X.T.dot(self.model() - self.Y)

    def gradient_descent(self, k):
        for i in range(1, 1000):
            self.theta = self.theta - 0.5 * self.gradient()
        self.result[:, k + 2] = self.theta[:, 0]


if __name__ == '__main__':
    file = pd.read_csv(sys.argv[1])
    i = 0
    houses = file["Hogwarts House"]
    for features in file.columns:
        if i < 6 or features == "Arithmancy" or features == "Potions" or features == "Care of Magical Creatures":
            del file[features]
        i += 1
    baza = np.array(file)
    Log_reg(baza, houses)