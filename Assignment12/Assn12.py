import numpy as np
import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

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
                               feature_names=cancer.feature_names,  # each node should include feature name
                               class_names=cancer.target_names,
                               filled=True)
    plt.title("Plot Tree")
    #plt.show()

   #I Program that generates multiple decision trees using the bagging. Draw a 2d Line plot
    #loop each time bagging score gets 1 value in estimator list
    n_estimators = [*range(1,21,1)]
    acc = []
    for item in n_estimators:
        bagging_score = BaggingClassifier(n_estimators=item).fit(X_train, y_train)
        accuracy = bagging_score.score(X_test, y_test)
        acc.append(accuracy)
    fig = plt.figure(figsize=(15, 10))
    plt.plot(n_estimators, acc)
    plt.title("Bagging Graph I")
    #plt.show()

    #J Program that generates multiple decision trees using the AdaBoost. Draw a 2D Line plot
    n_estimators = [*range(1, 21, 1)]
    acc = []
    for item in n_estimators:
        ada = AdaBoostClassifier(n_estimators=item, random_state=0)
        ada.fit(X_train, y_train)
        accuracy = ada.score(X_test, y_test)
        acc.append(accuracy)
    y_ada = acc
    x_ada = n_estimators #n_estimator = 20 lol ?

    fig = plt.figure(figsize=(15, 10))
    plt.plot(x_ada, y_ada)
    plt.title("Ada 2D Line Plot")
    #plt.show()


    #K Program that generates multiple decision trees using the random forest. Draw a 3D surface plot
    #for loop or loop
    n_estimators = [*range(1, 100, 1)]
    acc = []
    for item in n_estimators:
        classifier = RandomForestClassifier(max_depth=2, random_state=0)
        classifier.fit((X_train), (y_train))
        accuracy = classifier.score(X_test, y_test)
        acc.append([accuracy])
    z_forest_score = np.array(acc)
    y_axis = len(cancer.feature_names)
    x_axis = n_estimators #n estimators
    # graph
    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x_axis, y_axis, z_forest_score, cmap='viridis', edgecolor='none')
    plt.title("3D Graph")
    plt.show()
