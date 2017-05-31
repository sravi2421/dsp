# Python:  Introduction to Pandas    

## Objective
This section of the Python pre-work is intended to be an introduction to Pandas.  Explore the "Pandas Resources" links below for more advanced options.

## Introduction
### What is Pandas?

Pandas is a Python library for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.   

Pandas provides fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python.

### Pandas - the name
The name is derived from the term "Panel data", an econometrics term for multidimensional structured data sets.  

### What is a Pandas data frame?  
**DataFrame** is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.

---

## Pandas Resources
#### [Chris Albon (Data Wrangling section)](http://chrisalbon.com/)  
* [Chris Albon (Missing Data)](http://chrisalbon.com/python/pandas_missing_data.html)

#### [Greg Reda (Intro to Pandas Data Structures)](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/)  

#### [Things in Pandas I Wish I Had Known Sooner](http://nbviewer.jupyter.org/github/rasbt/python_reference/blob/master/tutorials/things_in_pandas.ipynb?utm_source=Python+Weekly+Newsletter&utm_campaign=8416b188e6-Python_Weekly_Issue_176_January_29_2015&utm_medium=email&utm_term=0_9e26887fc5-8416b188e6-312716773#Selecting-NaN-Rows)


---

## :boom: Exercises :boom:

>### Part 1:  Review Pandas Example
Review the Jupyter Notebook [`1_pandas_jeopardy_example.ipynb`](python/pandas/1_pandas_jeopardy_example.ipynb) which uses the `jeopardy.csv` data.

>### Part 2:  Try Pandas
* Open the Jupyter Notebook [`2_pandas_olive_questions.ipynb`](python/pandas/2_pandas_olive_questions.ipynb) which uses the `olive.csv` data.
* Make a copy of the notebook and name it `3_pandas_olive_answers_myname.ipynb`.  (Example:  my notebook would be called `3_pandas_olive_answers_reshama.ipynb`).
* Update the header at the top by adding in your name and date.
* Edit this notebook and complete the exercises.

---

## Optional Pandas Topics:  To Explore Further

* `groupby` objects
* applying functions
* indexing
* conditional selecting; filtering
* selecting rows and columns: `.loc`, `.iloc`, `.ix`
* working with missing data:  `Null`, `NaN`, `None`
* sorting
* merge, join
