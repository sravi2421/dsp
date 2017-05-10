# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 'ls', lists directory contents
'ls -a', includes directory contents that start with a dot (.).
'ls -l', List in long format (ie, lots of detail)
'ls -lh' List in long format, with shortened unit suffixes, ie GB, MB instead of total bytes
'ls -lah' List in long format, includes directory contents that start with a dot (.). With shorterened unit suffixes
'ls -t' Sorts by time modified
'ls -Glp' Colored long output; writes a '/' after each output if it is a directory


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 'ls -c' Displays files by file timestamp.
    'ls -C'	Displays files in a columnar format (default)
    'ls -R'	Displays subdirectories as well.
    'ls -t'	Displays newest files first. (based on timestamp)
    'ls -1'	Displays each entry on a line.


---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > The xargs utility reads space, tab, newline and end-of-file delimited
     strings from the standard input and executes utility with the strings as
     arguments.

     find temp/ "*.txt" -print0 | xargs -0 ls

     finds and prints all .txt files within the temp director 
