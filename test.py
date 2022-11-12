import os
import sys
from supervised.automl import AutoML
from sklearn import datasets
from sklearn.model_selection import train_test_split

project_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(project_path, 'model_persist')

def generate_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train,X_test,y_train,y_test = \
        train_test_split(X, y, train_size=0.8, stratify=y)
    return X_train,X_test,y_train,y_test

def train(X_train, y_train):
    ml_model = AutoML(
        results_path = model_path, 
        mode = 'Explain',
        optuna_time_budget=1
    )
    ml_model.fit(X_train, y_train)

def test(X_test,y_test):
    ml_model = AutoML(
        results_path = model_path, 
        mode = 'Explain',
        optuna_time_budget=1
    )
    print(ml_model.predict(X_test))
    print(y_test)

if __name__ == "__main__":
    if sys.argv[1] == 'train':
        X_train,X_test,y_train,y_test = generate_data()
        train(X_train, y_train)
    elif sys.argv[1] == 'test':
        X_train,X_test,y_train,y_test = generate_data()
        test(X_test, y_test)
    else:
        print('Check your argument, Only train and test are allowed!')
