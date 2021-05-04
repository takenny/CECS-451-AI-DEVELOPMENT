import numpy
import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.ensemble import BaggingClassifier
if __name__ == "__main__":
    cancer = sklearn.datasets.load_breast_cancer() #load dataset A
    print("Dataset Feature names are ", list(cancer.feature_names)) #print out features names B
    print("Target names are ", cancer.target_names) #print out target names B

    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.5) #allocate half data C
   # print(cancer.target.shape)
   # print(X_train.shape)
   # print(X_test.shape)
   # print(y_train.shape)
   # print(y_test.shape)
    clf = DecisionTreeClassifier(criterion='gini', max_depth=2) #F
    # G Write a Program that generates a decision tree
    tree = clf.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    print("The accuracy score of the classifier by comparing y_pred and y_test is ", accuracy_score(y_test, y_pred))

    #H Visualize the tree with plot_tree
    fig = plt.figure(figsize=(15, 10))
    _ = sklearn.tree.plot_tree(clf,
                       feature_names=cancer.feature_names, #each node should include feature name
                       class_names=cancer.target_names,
                       filled=True)
    plt.show()

    #I Program that generates multiple decision trees using the bagging. Draw a 2d Line plot


    #J Program that generates multiple deciison trees using the AdaBoost. Draw a 2D Line plot


    #K Program that generates multiple deciiosn trees using the random forest. Draw a 3D surface plot



