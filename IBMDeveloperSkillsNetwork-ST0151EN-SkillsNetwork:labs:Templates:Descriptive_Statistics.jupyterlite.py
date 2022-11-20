import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot


## read file ##
ratings_df=pd.read_csv(r"Datasets/teachingratings.csv")
print(ratings_df)

## display informantion about the datastet ##
ratings_df.head()
ratings_df.info()
ratings_df.shape

## Find the mean, median, minimum, and maximum values for students ##
print(ratings_df['students'].mean())
print(ratings_df['students'].median())

print(ratings_df['students'].min())
print(ratings_df['students'].max())

## Produce a descriptive statistics table ##
print(ratings_df.describe())

## plot histigram to analyze the 'beauty' column ##
pyplot.hist(ratings_df['beauty'])



## some statistics on the data using 'groupby' ##
print(ratings_df.groupby('gender').agg({'beauty':['mean', 'std', 'var']}).reset_index())

tenure_count = ratings_df[ratings_df.tenure == 'yes'].groupby('gender').agg({'tenure': 'count'}).reset_index()
print(tenure_count)

tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
print(tenure_count)

print(ratings_df.groupby('tenure').agg({'age':['mean', 'std']}).reset_index())

print(ratings_df.groupby('minority').agg({'tenure': 'count'}).reset_index())