import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

if __name__ == '__main__':
    test = [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08]
    name = ['sent1']
    df = pd.DataFrame(test, columns=name)

    print(df)
    print("Distances ", test)
    print("distances length ", len(test))
    ax = sns.boxplot(x=name, y=df[name], data=df)

    plt.show()