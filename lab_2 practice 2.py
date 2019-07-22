Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 10
>>> a = b
>>> b = a
>>> a
10
>>> b
10
>>> a = 5
>>> b = 10
>>> a = c
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a = c
NameError: name 'c' is not defined
>>> a = 5
>>> c = a
>>> a = b
>>> a
10
>>> b = c
>>> b
5
>>> four = 4
>>> print(four*3)
12
>>> five = 4
>>> print(5)
5
>>> print(five*3)
12
>>> my_name = 'ori'
>>> print("hi" + myname)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("hi" + myname)
NameError: name 'myname' is not defined
>>> print("hi" + myname')
	  
SyntaxError: EOL while scanning string literal
>>> my_name = "ori"
	  
>>> print("hi" = myname)
	  
SyntaxError: keyword can't be an expression
>>> print( "hi" + my_name )
	  
hiori
>>> print( "hi " + my_name )
	  
hi ori
>>> my_age = ‘15’
print( ‘ I am ‘ + my_age + ‘ years old’)
	  
SyntaxError: invalid character in identifier
>>> my_age = ‘15’
	  
SyntaxError: invalid character in identifier
>>> my_age = 15
print( “ I am “ + my_age + “ years old”)
	  
SyntaxError: multiple statements found while compiling a single statement
>>> my_age = 15
	  
>>> print( “ I am “ + my_age + “ years old”)
	  
SyntaxError: invalid character in identifier
>>> print( ' I am ' + my_age + ' years old')
	  
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print( ' I am ' + my_age + ' years old')
TypeError: must be str, not int
>>> print( “ I am “ + my_age + “ years old”)
	  
SyntaxError: invalid character in identifier
>>> print( “ I am “ + my_age + “ years old ”)
	  
SyntaxError: invalid character in identifier
>>> print(“ I am “ + my_age + “ years old ”)
	  
SyntaxError: invalid character in identifier
>>> print(“I am “ + my_age + “ years old ”)
	  
SyntaxError: invalid character in identifier
>>> prit("I am " + my_age + " years old")
	  
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    prit("I am " + my_age + " years old")
NameError: name 'prit' is not defined
>>> print("I am " + my_age + " years old")
	  
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print("I am " + my_age + " years old")
TypeError: must be str, not int
>>> my_age = 15
	  
>>> print("I am " + my_age + " years old")
	  
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print("I am " + my_age + " years old")
TypeError: must be str, not int
>>> my_age = "15"
	  
>>> print("I am " + my_age + " years old")
	  
I am 15 years old
>>> my_age = '15'
	  
>>> print("I am " + my_age + " years old")
	  
I am 15 years old
>>> score = 4
	  
>>> count = "5"
	  
>>> total = score * count
	  
>>> print(total)
	  
5555
>>> sscore = "4"
	  
>>> count = "5"
	  
>>> total = score * count
	  
>>> print(total)
	  
5555
>>> >>> total = (score * count)
	  
SyntaxError: invalid syntax
>>> total
	  
'5555'
>>> score*5
	  
20
>>> score= "4"
	  
>>> count = 5
	  
>>> score = 4
	  
>>> total = score * count
	  
>>> print(total)
	  
20
>>>  
