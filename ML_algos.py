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
    def __init__(self, ls):
        songs_csv = pd.read_csv(ls)
        x = songs_csv.iloc[:, 0:9]
        y = songs_csv.iloc[:, 9]
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

        ax = sns.stripplot(training)
        ax.set(xlabel='values of k', ylabel='Training Score')

        plt.show()

        ax = sns.stripplot(test)
        ax.set(xlabel='values of k', ylabel='Test Score')
        plt.show()

        plt.scatter(K, training, color='k')
        plt.scatter(K, test, color='g')
        plt.show()

    def dt_algo(self):

        clf = DecisionTreeClassifier()

        clf = clf.fit(self.X_train, self.y_train)

        y_pred = clf.predict(self.X_test)

        print("Accuracy:", metrics.accuracy_score(self.y_test, y_pred))

    def svm_algo(self):
        clf = svm.SVC(kernel='linear')
        clf.fit(self.X_train, self.y_train)
        y_pred = clf.predict(self.X_test)
        print("Accuracy:", metrics.accuracy_score(self.y_test, y_pred))

    def adaboost(self):

        abc = AdaBoostClassifier(n_estimators=50,
                                 learning_rate=1)
        model = abc.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        print("Accuracy:", metrics.accuracy_score(self.y_test, y_pred))
