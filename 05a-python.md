# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples serve similar functions and can be used to store multiple items.  Lists are mutable, which indicates that the individual values within a particular list can be changed (ie, the command list[0] = 3, would change the first value of a list to 3). This is different from tuples which are immutable.  In python, only tuples can be used as keys in dictionaries.  This is because dictionaries in python are implemented as hasthables and in order to get the performance of a hashtable, you must only use immutable objects as keys since each key must 'hash' to the same value every time it is called, something that is not possible with mutable objects.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are mutable, which means that you can change specific elements within them whereas sets are immutable.  You can index into and out of lists whereas you can't with sets. Sets can only be used when the order of items which you are storing does not matter. Performance for a list is slower than a set since it is in O(n) where as it is O(1) in sets.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are used within python when you need the functionality of a function but are only going to use the operation once.  Below is a sample of a lambda function passed into the sorted function which will sort odd numbered numbers in a list before even numbers.

sorted(list, key = lambda x:(-(x%2, x)))

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions is a way to create some sort of functionality in a list to iterate through multiple elements in a list (or just a range of numbers) and then place the output in a list.  Below is a basic example:
S = [x**2 for x in range(10)]                               ## List comprehension
S = map(square, range(0,10))                                ## Map of same list, assuming there is a function named square which has been created
S = map(lambda x: x**2, range(0,10))                        ## Map of same list, using a lambda function
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

S = filter(f, [x**2 for x in range(10)])                    ## Filter to only show numbers on the list which are even
S = filter(lambda x: x%2 ==0, [x**2 for x in range(10)])    ## Filter to only show numbers on the list which are even
S = [0, 4, 16, 36, 64]

S = {x**2 for x in range(10)}                               ## Set comprehension

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
>> refer to python/q5_datetime.py

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> refer to python/q5_datetime.py

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> refer to python/q5_datetime.py

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
