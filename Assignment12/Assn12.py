import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    cancer = sklearn.datasets.load_breast_cancer() #load dataset A
    print("Dataset Feature names are ", list(cancer.feature_names)) #print out features names B
    print("Target names are ", cancer.target_names) #print out target names B

    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.5)
   # print(cancer.target.shape)
   # print(X_train.shape)
   # print(X_test.shape)
   # print(y_train.shape)
   # print(y_test.shape)
    clf = DecisionTreeClassifier(criterion='gini', max_depth=2)
    tree = clf.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    sklearn.tree.plot_tree

    print("The accuracy score of the classifier by comparing y_pred and y_test is ", accuracy_score(y_test, y_pred))


