import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import svm
from sklearn.ensemble import AdaBoostClassifier

knn_model = KNeighborsRegressor(n_neighbors=3)


class ML_algos:
    """
    ls: csv file path.
    header_size: number of properties for each track.
    """

    def __init__(self, ls, header_size):
        songs_csv = pd.read_csv(ls)
        x = songs_csv.iloc[:, 0:header_size - 1]
        y = songs_csv.iloc[:, header_size - 1]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            x, y, test_size=0.3, random_state=0)

    def knn_algo(self):

        K = []
        training = []
        test = []
        scores = {}

        for k in range(2, 21):
            clf = KNeighborsClassifier(n_neighbors=k)
            clf.fit(self.X_train, self.y_train)

            training_score = clf.score(self.X_train, self.y_train)
            test_score = clf.score(self.X_test, self.y_test)
            K.append(k)

            training.append(training_score)
            test.append(test_score)
            scores[k] = [training_score, test_score]

        for keys, values in scores.items():
            print(keys, ':', values)

        plt.scatter(K, training, color='k')
        plt.scatter(K, test, color='g')
        plt.show()

    def dt_algo(self):
        clf = DecisionTreeClassifier(random_state=0, max_depth=5)
        # clf = DecisionTreeClassifier(random_state=0)

        clf.fit(self.X_train, self.y_train)

        print("Test Accuracy:", clf.score(self.X_test, self.y_test))
        print("Trainning Accuracy:", clf.score(self.X_train, self.y_train))

    def svm_algo(self):
        clf = svm.SVC(kernel='linear')
        clf.fit(self.X_train, self.y_train)

        print("Test Accuracy:", clf.score(self.X_test, self.y_test))
        print("Trainning Accuracy:", clf.score(self.X_train, self.y_train))

    def adaboost(self):

        clf = AdaBoostClassifier(n_estimators=50,
                                 learning_rate=1)
        model = clf.fit(self.X_train, self.y_train)

        print("Test Accuracy:", clf.score(self.X_test, self.y_test))
        print("Trainning Accuracy:", clf.score(self.X_train, self.y_train))
