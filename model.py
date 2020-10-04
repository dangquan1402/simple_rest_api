import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score

def main():
    wine = load_wine()
    data = pd.DataFrame(data= np.c_[wine['data'], wine['target']],
                     columns= wine['feature_names'] + ['target'])

    X_train = data[:-20]
    X_test = data[-20:]

    y_train = X_train.target
    y_test = X_test.target

    X_train = X_train.drop('target',1)
    X_test = X_test.drop('target',1)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    import pickle
    pickle.dump(clf, open('models/final_prediction.pickle', 'wb'))


if __name__ == '__main__':
    main()