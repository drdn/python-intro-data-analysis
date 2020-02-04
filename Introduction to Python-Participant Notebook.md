
# Introduction to Python<br>Basics of Data Analysis Using Pandas

David Durden, Data Services Librarian <br>
Yishan Ding, Statistical Consulting Graduate Assistant

<img src="assets/python-logo.png" alt="Python Logo" width="200" align="right"/>

---

## What is Python?

- An interpreted high-level general-purpose programming language
- Both a programming language and a tool that executes scripts written in Python
- Python was created Guido van Rossum and released in 1991

<img src="assets/guido.png" alt="Guido van Rossum" width="100" align="right"/>

## Why use Python?

- Free
- Open-source with active development
- Available on all major OS's (MacOS, Linux, Windows)
- Large community
- Easy-to-learn*
- Encourages re-use and reproducibility
- Interdisciplinary and extensible

---

## Species of Python
[Anaconda](https://www.anaconda.com/) is a specific distribution of Python that includes a lot of popular packages by default, including IPython console, Jupyter Notebook, Pandas, and others.

Several OS's come with Python installed by default. However, the system Python is often used by the operating system. Modifying the system Python *can* result in some programs not working correctly.

---

## Outline for Today's Workshop
- [Some basic Python commands](#start)
- [Introduction to Pandas for data analysis](#pandas)
- [Data import and preview](#import)
- [Subsetting data](#subset)
- [Summary statistics and reporting](#sumrep)
- [Simple plots](#plots)
- [Simple Linear Regression](#model)

### Exercises
- [Exercise 1](#ex1)
- [Exercise 2](#ex2)
- [Exercise 3](#ex3)
- [Exercise 4](#ex4)
- [Exercise 5](#ex5)
- [Exercise 6](#ex6)

---

## Set Up Your Environment

We will be using a Jupyter Notebook for this workshop to avoid having to edit text files and execute them at the Command Line.

Python can also be run in interactive mode: You can type commands directly into the Python interpreter and see results. Open your Command Prompt or Terminal application and type `python`.

Using the interpreter is useful for testing code and getting immediate results. However, you cannot easily edit those commands or save your work. 

### Creating Python Scripts
Instead of using the interpreter, we can also write Python programs and then run them.

To get started, use a plain text editor like:
- [BBedit](https://www.barebones.com/products/bbedit/index.html)
- [Atom](https://atom.io/)
- [Notepad++](https://notepad-plus-plus.org/)

Text documents should be set up a specific way in order to read a valid Python code.
- The first line of your document should always be: `#! /usr/bin/env python`
- Save your file with `.py`

When you have written a program, you can run it using the following basic command: `python my_program.py`

---

## Getting Started<a name='start'></a>

- Meet the print statement
    - `print("Hello World!")`


```python
# Enter the 'hello world' print statement below
print("Hello World!")
```

    Hello World!


>**Fun fact**: Printing `Hello world!` to the screen is a rhetorical function used by programmers to test that their systems are operating correctly. Incidentally, this has also become one of the first programs that you learn in almost every programming language. The creation of this function is attributed to Brian Kernighan, who first published it in a code snippet in *A Tutorial Introduction to the Programming Language B* in 1973.

### Assign values to a variable
You can store anything in a variable in Python. 
- `x = 3 # Assign a single integer value`
- `y = [1, 2, 3] # Assign a list of integer values`
- `z = ["a", "b", "c"] # Assign a list of character values`
- `a = [y, z] # Assign a list of variables`
- `b = a # Assign a variable to a variable`

>TIP: You can either 'call' a variable directly or print it using the `print()` function.


```python
# Explore creating variables and assigning values below
# Experiment with calling the variable directly and printing it to the screen

```

### Using Python as a Calculator

- `35*40/4`
- `((6-4)*(2+8))/5`
- Advanced mathematical concepts are implemented in the `math` library which needs to be imported before we can use it
    - `from math import sqrt`
    - `sqrt(2)`


```python
# Do some arithmetic below!

```


```python
# Import the sqrt method from the math library and then calcuate a square root below

```

### 5 Basic Data Types

Certain Python operations require input to be of a specific data type.

Type     | Example
--------- | -------
Integer   | `3` or `int(3)`
Float     | `3.1415` or `float(6/5)`
Character | `"a"`, `"b"`, `"University of Maryland"` or `str()`
Logical   | `True`, `False` or `bool()`
Complex   | `1+4j` or `complex(1, 4)`

- To determine an object type, use `type()`
- To test if an object is a specific type, use `isinstance(object, type)`
- To change type, use `int()`, `float()`, `str()`, `bool()`, `complex()`



```python
# Test the number 3 with type()
# What's the result?

```


```python
# What will be returned if you run type(3.1415)?

```


```python
# Character or strings have to be wrapped in either single or double quotations
# Test the following string: Testudo

```


```python
# Store the ratio 6/5 in the variable foo
# Determine if foo is a float using the isinstance() method

```


```python
# Create a complex number using the complex() method

```

---

## Pandas: The Python Data Analysis Library<a name='pandas'></a>

[Pandas](https://pandas.pydata.org/) is already included by default in Anaconda Python. If you are using a different distribution you will have to download and install Pandas.

> Pandas provides easy-to-use methods for working with data structures and performing data analysis using the Python language and enviroment.

> Many of the commands and capabilities are similar to R.

We have to import Pandas before we can use, similar to how we imported the `math` library
- `import pandas`
- `import pandas as pd`



```python
# To get started using Pandas we have to import it first
# Import Pandas using the import statment

# Imported libraries can be aliased to make code shorter and easier to type
# pd is the common alias for Pandas
# Import Pandas and alias it as pd

# Below is an optional parameter to limit the amount of rows printed to the screen
# Uncomment it to enable it
#pd.set_option('display.max_rows', 10) 
```

### Basic Commands

These are the basic commands when working with DataFrames in Pandas.


- `df.max()`
- `df.min()`
- `df.mean()`
- `df.median()`
- sum
    - `df.sum()`
    - `df.cumsum()`
- `df.var`
- `df.std()`
- length
    - `len(df.index) # Returns the length of the index column`
    - `df.count()`
- summary
    - `df.describe()`

## Import a Dataset<a name='import'></a>

We will begin by importing the `GSSsubset.csv` file.

Pandas uses the `pandas.read_csv()` function to import csv files.
>File names are string data and should be wrapped in quotes!


```python
# Note you should use pd.read_csv() because we imported pandas as pd!
# Import the GSSsubset.csv file below

```

### Let's Examine a Dataset

When importing a dataset we should assign it to a variable for future use.

Declare a variable name and assign the `read_csv()` function from earlier.


```python
# df is common short hand in Pandas for "DataFrame", which is the object type
# created when importing a csv file
# Using the pd.read_csv() statement from above, store the dataframe in a variable named gss_df

```

### Preview the First Few Lines of a Dataset
After we assign our dataset to a variable, we can preview it with `head()`

Syntax: `dataFrame.head()`


```python
# Preview the first few lines of the dataframe with head()

```

### Examine a Dataset

`head()` let's us look at the first few lines of a file.

`tail()` will let us look that last few lines of a file.

`describe()` will give us summary information.


```python
# Preview the last few lines of the dataframe with tail()

```


```python
# Print summary statistics for the dataframe using describe()
# Try printing the results of describe() instead of calling the method directly on the dataframe

```

---

## Exercise 1: Examine a Dataset<a name='ex1'></a>

- Import the dataset `car.csv`
- Preview the dataset
    - Call the variable that you assigned to `car.csv`
    - Call the `head()` function on the DataFrame


```python
# Import the dataset car.csv and assign it to the variable 'car'

```


```python
# Preview the dataset with dataFrame.head()

```

---

## Examine the Dataset
Where `df` is the name of your DataFrame:
- `df.shape` 
    - Returns row x column
- `df.columns`
    - Returns a list of the column names
- `df.index`
    - Returns row information (range and step)
- `df.info()`
    - Returns list of variables, data type, count, size, etc.



```python
# Examine the car Dataset

```

## Exercise 2: Examine the Dataset<a name='ex2'></a>
- Examine the dimensions of `car.csv`
    - How many rows does this dataset have?
    - How many columns?
    - What are the variable names?


```python
# What is the shape of the dataframe?

```


```python
# What are the column names?

```


```python
# What are the row names (indeces)?

```


```python
# What are the data types for each variable?
# Hint: Use info()

```


```python
# Print the summary statistics for the dataframe

```

---

## Subset the Dataset<a name='subset'></a>
Refer to [this](https://cmdlinetips.com/2019/03/how-to-select-one-or-more-columns-in-pandas/) article for a more in-depth explanation of subsetting in Pandas.

|1. Subset by row/column name|2. Subset by row/column index
|:---|:---|:---|:---|
|**`df.loc[rowname, colname]`**|**`df.iloc[rowindex, colindex]`**|
|- `df.loc[2, 'degree']`<br>- `df.loc[:3,'id':'income']`<br>- `df.loc[[1,3,5],['id', 'degree', 'income']`|- `df.iloc[1, 3]`<br>- `df.iloc[:5,]`<br>- `df.iloc[900:, [2,3,5,8]]`|


```python
# Here is an example of a subset of all records for variables sex through income
gss_df.loc[0:, 'sex':'income']
```

### Subset the Dataset
|3. Subset by variable name|4. Subset by specific criteria|
|:---|:---|
|**`df['colname']`**<br>**`df.colname`**|**`data[data['variable'] <operator> 'criteria']`**|
|- `data['id']`<br> - `data[['id', 'degree', 'income']]`<br>- `data.degree`|- `data[data['age'] < 50]`<br>- `data[data['sex'] == 'MALE']`<br>- `data[(data['age'] < 50) & (data['sex'] == 'MALE')]`|


```python
# Here is an example of a subset for males less than 50 years of age
# Note that this expression includes the head() method...
gss_df[(gss_df['age'] < 50) & (gss_df['sex'] == 'MALE')].head()
```

---

## Exercise 3<a name='ex3'></a>

Using the dataset `car.csv`, create subsets that meet the following criteria: 

 - Include only cars made from USA
     - Name this new subset data to be `usacar`. 
     - How many cars do this new dataset contain?


```python
# Input your code below

```

Answer (highlight to reveal): <font color='white'>147</font>

- Include cars that are made from USA AND their MSRP is larger than $40,000. 
     - Name this new subset data to be `usa40k`. 
     - How many cars do this new dataset contain? 


```python
# Input your code below

```

Answer (highlight to reveal): <font color='white'>25</font>

---

## Summary Report<a name='sumrep'></a>
- Summary of each variable: `df.describe()`
- Summary statistics for subgroups/categories: 
    - **Example question:** According to this dataset, what is the average income by sex?


```python
# Calculate the mean using the aggregate() method and the mean function
print(gss_df.groupby(['sex'])[['income']].aggregate('mean'))
```


```python
# Call the mean() method directly on the income variable
gss_df.groupby('sex')['income'].mean()
```

---

## Exercise 4: Answering Questions with Data<a name='ex4'></a>
- Based on the `car.csv` dataset, what is the average MSRP for cars made from Asia, Europe and USA, respectively?


```python
# Input your code below

```

Answer (highlight to reveal): <font color='white'>24741.32, 48349.80, 28377.44</font>

---

## Plotting in Python/Pandas<a name='plots'></a>
We need to import `matplotlib`, a popular scientific plotting library


```python
# This command forces plots to display in Jupyter Notebooks
%matplotlib inline 
# This command imports matplotlib and assigns the alias plt
import matplotlib.pyplot as plt
```

### Univariate Graph: Histogram
More information on plotting historgrams [here](https://pythonspot.com/matplotlib-histogram/)


```python
# Graph the data
plt.hist(gss_df['income'], edgecolor='black', linewidth='1', alpha=0.5)
# Add title and axes labels
plt.title('Histogram of Income')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
```

### Another way to Create a Histogram
The `plot()` function is useful for when you don't want to mess with the aesthetics of graph.


```python
gss_df['income'].plot(kind='hist', title='Histogram of Income').set(xlabel='Annual Income')
```

### Univariate Graph: Bar Chart


```python
# To plot a single variable on a bar chart, we need
# to count the individual values first
gss_df['marital'].value_counts().plot(kind='bar')
```

### Bivariate Graph: Scatterplot


```python
# Graph the data
plt.scatter(gss_df['hrswrk'], gss_df['income'])
# Set the axes and title labels
plt.title('Plot of Income and Working Hours')
plt.xlabel('Working Hours')
plt.ylabel('Annual Income')
```

## Exercise 5: Plot Some Data<a name='ex5'></a>

Using `car.csv`, 

1. Plot a histogram on MSRP
2. Plot a bar chart on car’s Origin 
3. Draw a scatter plot showing the relation between MSRP (Y axis) and Horsepower (X axis)


```python
# Plot the histogram on MSRP

```


```python
# Plot a bar chart on car’s Origin

```


```python
# Draw a scatter plot showing the relation between MSRP (Y axis) and Horsepower (X axis)

```

---

## Simple Linear Regression<a name='model'></a>
<center>${y} = \beta_0+\beta_1{x}+{e}$</center>
- ${y}$ : dependent variable
- ${x}$ : independent variable
- ${e}$ : error term
- $\beta_0$ : intercept
- $\beta_1$ : slope

1. **F-test ${p}$-value**: *Is this model statistically significant?*
2. **${r}^2$**: *How much variance in ${y}$ can be explained by the variance in ${x}$?*
3. **Intercept**
4. **Slope**

### Linear Regressions using statsmodels.formula.api


```python
import statsmodels.formula.api as smf

# This is the easier way of implementing a linear model using
# R-like formulas with the patsy package
# Note the lowercase 'ols' (required to use patsy formulae)
model = smf.ols(formula='income ~ hrswrk', data=gss_df).fit() 
print(model.summary())                                        
```

---

## Exercise 6<a name='ex6'></a>

Using the `car.csv` data, answer the following questions:

 - Run a simple linear regression explaining MSRP by Horsepower
     - Store your model in a variable named 'mod'
     - Print the summary of your model to the screen
     - Using the regression output, write down the model equation as comment in your script
 - Is the model significant on alpha = 0.05? 


```python
# Input your code below

```

---

## Thank you!



### David Durden
✉️ [durden@umd.edu](mailto:durden@umd.edu)<br>
🖥 [https://lib.umd.edu/data]()

### Yishan Ding
✉️ [ysding@umd.edu](mailto:ysding@umd.edu)<br>
🖥 [https://lib.umd.edu/rc/statistical-consulting]()
