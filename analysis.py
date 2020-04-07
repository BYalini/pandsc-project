# Project : Iris Data Set Exploration
# Iris data set is introduced by the British statistician and biologist Ronald Fisher
# The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). 
# Four features(variables) were measured for each sample:  the length and the width of the sepals and petals, in centimeters.
# Ref : https://en.wikipedia.org/wiki/Iris_flower_data_set
# Ref: redirecting print output to file https://realpython.com/python-print/#printing-to-a-file

import pandas as pd

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