# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference.

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

---

### Part I - Regular Expressions  


#### Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> There are 27 professors who hold only a PhD, 5 with just a ScD, and another four professors who hold more than one degree.

>> Code is jupyter notebook python/Metis_adv_python_prework

#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> There are three titles, Professor(13), Associate Professor(12), and Assistant Professor(12)

>> Code is jupyter notebook python/Metis_adv_python_prework

#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> Code is jupyter notebook python/Metis_adv_python_prework


#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>>  mail.med.upenn.edu    23
    upenn.edu             12
    cceb.med.upenn.edu     1
    email.chop.edu         1

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

>> Code is jupyter notebook python/Metis_adv_python_prework

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

>> Code is jupyter notebook python/Metis_adv_python_prework

---

### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> Code is jupyter notebook python/Metis_adv_python_prework

#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> Code is jupyter notebook python/Metis_adv_python_prework

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> Code is jupyter notebook python/Metis_adv_python_prework

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

---

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)
