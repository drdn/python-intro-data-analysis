#! /usr/bin/env python

#--------------------------------------
#
# Supplementary code for
# Introduction to Python: 
# Basics of Data Analysis Usings Pandas
#
# Created by David Durden and Yishan Ding
# 2019-10-08
#
#--------------------------------------

# Import necessary libraries
import pandas as pd
pd.set_option('display.max_rows', 10)
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

#----------------
# Exercise 1
#----------------
car = pd.read_csv("data/car.csv")   # Store the car dataset in a variable

#----------------
# Exercise 2
#----------------
car.head()      # Preview the dataset
car.describe()  # Print the summary of the dataset
car.shape()     # Return dimensions of the dataset
car.columns()   # Return a dictionary column names
car.info()
car.index()     # Return a data types for each variable

#----------------
# Exercise 3
#----------------
usacar = car[car.Origin == "USA"]
usacar.shape[0]

usa40k = car[(car.Origin == "USA") & (car.MSRP > 40000)]
usa40k.shape[0]

#----------------
# Exercise 4
#----------------
car.groupby("Origin")["MSRP"].mean()     # Group cars by origin and calculate  
                                        # the mean for the MSRP variable
car.groupby("Origin", as_index=False)["MSRP"].mean()    # Group cars by origin and
                                                        # calculate the mean for MSRP
                                                        # and format the results
                                                        # as a table
car.groupby(["Origin"])[["MSRP"]].aggregate("mean")  # Group cars by origin and
                                                    # then aggregate on the mean 
                                                    # of the MSRP

#----------------
# Exercise 5
#----------------
plt.hist(car.MSRP)              # Plot a histogram of MSRP using matplotlib
plt.title("Histogram of MSRP")  # Set the title
plt.xlabel("MSRP")              # Set the label of the x axis
plt.ylabel("Frequency")         # Set the label of the y axis

# Plot a histogram using Pandas
car.MSRP.plot(kind = "hist", title = "Histogram of MSRP").set(xlabel = "MSRP")

# Plot a bar chart of the Origin variable using Pandas
car.Origin.value_counts().plot(kind = 'bar')

# Plot a scatter plot using matplotlib
plt.scatter(car.Horsepower, car.MSRP)
plt.title("Plot of MSRP and Horsepower")
plt.xlabel("Horsepower")
plt.ylabel("MSRP")

#----------------
# Exercise 6
#----------------
mod = smf.ols('MSRP ~ Horsepower', data = car).fit()    # Model a linear regression
                                                        # using the statsmodel library
print(mod.summary())    # Print the results of the regression
