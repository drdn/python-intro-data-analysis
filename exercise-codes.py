#! /usr/bin/env python

#--------------------------------------
#
# Exercise code for
# Introduction to Python: 
# Basics of Data Analysis Usings Pandas
#
# Created by David Durden and Yishan Ding
# 2019-07-23
#
#--------------------------------------

from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
pd.set_option('display.max_rows', 10)

#----------------
# Exercise 1: Import a Dataset
#----------------
# Import the ISBN.csv dataset
isbn = pd.read_csv("data/ISBN.csv")     # for MacOS/Unix
# isbn = pd.read_csv("data\ISBN.csv")   # for Windows

print(isbn.head())      # Preview the dataset

#----------------
# Exercise 2: Examine a Dataset
#----------------
# Preview the dataFrame
print(isbn.shape())     # What is the shape of the dataFrame?
print(isbn.columns())   # What are the column names?
print(isbn.index())     # What are the row (index) names?
print(isbn.info())      # What are the data types for each variable?
print(isbn.describe())  # What are the summary statistics for this dataFrame?

#----------------
# Exercise 3
#----------------
# In which yearrs was the Journal of Crystal Growth requested?
# Sort the dataFrame
isbnSorted = isbn.sort_values(by=['year'], inplace=False, ascending=False)
# Subset by journal_title
jcg = isbn[(isbn['journal_title'] == 'Journal of Crystal Growth')]
# Select only the title and year columns
jcgSub = jcg.loc[:, ['journal_title', 'year']]
print(jcgSub)

#----------------
# Exercise 4
#----------------
# Import lib_checkout.csv
libdata = pd.read_csv("data/lib_checkout.csv")  # for MacOS/Unix
#libdata = pd.read_csv("data\lib_cehckout.csv") # for Windows

# How many books were checked out by undergrads
libdata.groupby(['status'])[['book_checkout']].aggregate('sum')
# How many books were checked out by graduate students
libdata.groupby(['status'])[['book_checkout']].aggregate('sum') # Technically redundant
                                                                # Script returns both numbers
# How many books were checked out by day of the week on average?
libdata.groupby(['day'])[['book_checkout']].aggregate('mean')
# Bonus: total book_checkout in a one-liner
# Assign to the variable weekmean
weekmean = libdata[['book_checkout']].aggregate('sum')
#----------------
# Exercise 5: Simple Scatterplot
#----------------
# Plot libdata as a scatterplot with 'laptop_checkout' as x and 'book_checkout' as y
# for undergraduates only
undergrads = libdata[libdata['status'] == 'Undergrad']
plt.scatter(undergrads['laptop_checkout'], undergrads['book_checkout'])
plt.show()

#----------------
# Exercise 6: Plot a Simple Linear Regression
#----------------
# Use the statsmodels.formula.api library
# Use the lowercase ols (ordinary least squares)
#y = ulib['book_checkout']      # dependent variable
#x = ulib['laptop_checkout']    # independent variable
model = smf.ols(formula='book_checkout ~ laptop_checkout', data=ulib).fit()
print(model.summary())