import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")


sns.scatterplot(x="sepal_length", y="sepal_width", data=iris)

plt.show()

sns.pairplot(iris)

plt.show()

sns.violinplot(x="species", y="petal_length", data=iris)

plt.show()

sns.boxplot(x="species", y="petal_width", data=iris)

plt.show()
