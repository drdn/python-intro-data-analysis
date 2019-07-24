#! /usr/bin/env python

#--------------------------------------
#
# Supplementary code for
# Introduction to Python: 
# Basics of Data Analysis Usings Pandas
#
# Created by David Durden and Yishan Ding
# 2019-07-23
#
#--------------------------------------

# Import necessary libraries
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
pd.set_option('display.max_rows', 10)

#----------------
# Hello, World!
#----------------
print("Hello, World!")

#----------------
# Create some varialbes
#----------------
x = 3               # Assign a single integer value
y = [1, 2, 3]       # Assign a list of integer values
z = ["a", "b", "c"] # Assign a list of character values
a = [y, z]          # Assign a list of variables
b = a               # Assign a variable to a variable

print(x, y, z, a, b, sep='\n') # Prints all of the variables with each on a newline

#----------------
# Use Python as a Calculator
#----------------
print(35*40/4)
print(((6-4)*(2+8))/5)
print(sqrt(2))

#----------------
# Data Types
#----------------
print(type(3))                  # Returns int
print(type(3.1415))             # Returns float
print(type("Testudo"))          # Returns str
foo = 6/5
print(isinstance(foo, float))   # Returns true
print(complex(1, 4))            # Returns 1+4j

#----------------
# Basic Pandas Commands
#----------------
# Create a sample dataFrame so that the code will run
df = pd.DataFrame(np.array([np.arange(10)]*3).T, columns=['A', 'B', 'C'])
print(df.max())
print(df.min())
print(df.mean())
print(df.median())
print(df.sum())
print(df.std())
print(len(df))
print(df.count())
print(df.describe())

#----------------
# Import a Dataset
#----------------
# Assumes that the script is being run from the same directory as the data file
pd.read_csv("data/GSSsubset.csv")   # for MacOs/Unix
#pd.read_csv("data\GSSsubset.csv")  # for Windows

# Store the dataFrame in a variable
gss_df = pd.read_csv("data/GSSsubset.csv")   # for MacOs/Unix
#gss_df = pd.read_csv("data\GSSsubset.csv")  # for Windows

print(gss_df.head())
print(gss_df.tail())
#gss_df.describe()
print(gss_df.describe())

#----------------
# Subsetting
#----------------
# Create a subset of the GSSsubset.csv dataFrame
# Select only those rows of males under the age of 50
gss_sub = gss_df[(gss_df['age'] < 50) & (gss_df['sex'] == 'MALE')]
print(gss_sub.head())

#----------------
# Plotting Data
#----------------

# Univariate Histogram
# Graph the data
plt.hist(gss_df['income'], edgecolor='black', linewidth='1', alpha=0.5)
# Set the title and axes labels
plt.title('Histogram of Income')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
plt.show()  # The show plot method is not included in the Jupyter Notebook
            # which instead uses %matplotlib inline

# Alternate code for a histogram
gss_df['income'].plot(kind='hist', title='Histogram of Income').set(xlabel='Annual Income')
plt.show()

# Univariate Bar Chart
# To plot a single variable on a bar chart, we need to count the individual values 
# using .value_counts()
# Graph the data
gss_df['marital'].value_counts().plot(kind='bar')
plt.show()

# Bivariate Scatterplot
# Graph the data
plt.scatter(gss_df['hrswrk'], gss_df['income'])
# Set the title and axes labels
plt.title('Plot of Income and Working Hours')
plt.xlabel('Working Hours')
plt.ylabel('Annual Income')
plt.show()

#----------------
# Linear Regressions
#----------------
# There are two ways to fit a linear model using statsmodels
# One requires manually setting the constant
# The other does it for you and uses 'R-like' formulae

# The hard way using statsmodels.api
y1 = gss_df['income']               # Dependent variable
x1 = gss_df['hrswrk']               # Independent variable
y1, x1 = np.array(y1), np.array(x1) # Convert to numpy arrays
x1 = sm.add_constant(x1)            # Add constant (column of 1's)
model = sm.OLS(y1, x1)              # Define the model; note the use of uppercase OLS
fitted = model.fit()                # Fit the model
print(fitted.summary())             # Print the results

# The easier way using statsmodels.formula.api
model1 = smf.ols(formula='income ~ hrswrk', data=gss_df).fit()  # Note the use of lowercase ols
print(model1.summary())