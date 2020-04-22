# Project : Iris Data Set Exploration
# Iris data set is introduced by the British statistician and biologist Ronald Fisher
# The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). 
# Four features(variables) were measured for each sample:  the length and the width of the sepals and petals, in centimeters.
# Ref : https://en.wikipedia.org/wiki/Iris_flower_data_set
# Ref: redirecting print output to file https://realpython.com/python-print/#printing-to-a-file
# Ref : https://seaborn.pydata.org/tutorial/distributions.html
# Ref : https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# Ref : https://seaborn.pydata.org/generated/seaborn.pairplot.html

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read Iris.Data csv file into pandas datframe
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv('iris.data', names = col_names)

# write summary statistics of the dataset to file 
with open('summary.txt', mode='w') as file_summary : 
    print("Summary statistics: All species", file=file_summary)
    print(iris_df.describe(), file=file_summary)
    print("", file=file_summary)  # insert blank line
    # select only the wrong with Iris-setosa species
    print('Summary statistics: Iris-setosa', file =file_summary)
    print(iris_df[iris_df['species'] == 'Iris-setosa'].describe(), file = file_summary)
    print("", file=file_summary)  # insert blank line
    # select only the wrong with Iris-virginica species
    print('Summary statistics: Iris-virginica', file =file_summary)
    print(iris_df[iris_df['species'] == 'Iris-virginica'].describe(), file = file_summary)
    print("", file=file_summary)  # insert blank line
    # select only the wrong with Iris-versicolor species
    print('Summary statistics: Iris-versicolor', file =file_summary)
    print(iris_df[iris_df['species'] == 'Iris-versicolor'].describe(), file = file_summary)
    
# plt histograms of each data and save as png
fig = plt.figure()
plt.hist(iris_df['sepal_length'])
plt.xlabel('sepal length in cm')
plt.ylabel('Frequency')
plt.savefig('sepal_length_hist.png')

fig = plt.figure()
plt.hist(iris_df['sepal_width'])
plt.xlabel('sepal width in cm')
plt.ylabel('Frequency')
plt.savefig('sepal_width_hist.png')

fig = plt.figure()
plt.hist(iris_df['petal_length'])
plt.xlabel('petal length in cm')
plt.ylabel('Frequency')
plt.savefig('petal_length_hist.png')

fig = plt.figure()
plt.hist(iris_df['petal_width'])
plt.xlabel('petal width in cm')
plt.ylabel('Frequency')
plt.savefig('petal_width_hist.png')

#histogram of each variable differentiation each species
fig = sns.FacetGrid(iris_df,hue='species',height=5).map(sns.distplot,'sepal_length', kde=False).add_legend()
fig.set(xlabel='sepal length in cm', ylabel='Frequency')
fig.savefig('sepal_length_snshist.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(sns.distplot,'sepal_width', kde=False).add_legend()
fig.set(xlabel='sepal width in cm', ylabel='Frequency')
fig.savefig('sepal_width_snshist.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(sns.distplot,'petal_length', kde=False).add_legend()
fig.set(xlabel='petal length in cm', ylabel='Frequency')
fig.savefig('petal_length_snshist.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(sns.distplot,'petal_width', kde=False).add_legend()
fig.set(xlabel='petal width in cm', ylabel='Frequency')
fig.savefig('petal_width_snshist.png')

#scatter plot each pair while diffentiating based on species
fig = sns.FacetGrid(iris_df,hue='species',height=5).map(plt.scatter,'sepal_length','sepal_width').add_legend()
fig.set(xlabel='sepal length in cm', ylabel='sepal width in cm')
fig.savefig('sepal_length_vs_sepal_width.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(plt.scatter,'sepal_length','petal_length').add_legend()
fig.set(xlabel='sepal length in cm', ylabel='petal length in cm')
fig.savefig('sepal_length_vs_petal_length.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(plt.scatter,'sepal_length','petal_width').add_legend()
fig.set(xlabel='sepal length in cm', ylabel='petal width in cm')
fig.savefig('sepal_length_vs_petal_width.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(plt.scatter,'sepal_width','petal_length').add_legend()
fig.set(xlabel='sepal width in cm', ylabel='petal length in cm')
fig.savefig('sepal_width_vs_petal_length.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(plt.scatter,'sepal_width','petal_width').add_legend()
fig.set(xlabel='sepal width in cm', ylabel='petal width in cm')
fig.savefig('sepal_width_vs_petal_width.png')

fig = sns.FacetGrid(iris_df,hue='species',height=5).map(plt.scatter,'petal_length','petal_width').add_legend()
fig.set(xlabel='petal length in cm', ylabel='petal width in cm')
fig.savefig('petal_length_vs_petal_width.png')

# Pair plot gives all possible combinations of x and y as scatter plot and histogram in one image
# sns.pairplot(iris_df, hue='species')
fig = sns.pairplot(iris_df, hue='species', diag_kind = 'hist', markers=['o', 's', 'D'])
fig.savefig('hist_and_scatter.png')
