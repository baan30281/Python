Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from_future_import division
SyntaxError: invalid syntax
>>> 1/2
0.5
>>> 3/4
0.75
>>> 3//4
0
>>> 2 % 5
2
>>> 2 % 7
2
>>> 10 % 7
3
>>> 2 ** 2
4
>>> 2** 5
32
>>> ox1a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ox1a
NameError: name 'ox1a' is not defined
>>> 0x1a
26
>>> x=3
>>> x*3
9
>>> input("enter number x:")
enter number x: 45
' 45'
>>> x=input("enter number x")
enter number x4
>>> x
'4'
>>> if 1==2 print("my god")
SyntaxError: invalid syntax
>>> if 1==2: print("my god")

>>> 
>>> 
>>> pow(2,5)
32
>>> 10+pow(2,3*5)/3.0
10932.666666666666
>>> from math import sqrt
>>> sqrt(100)
10.0
>>> from future import division
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    from future import division
ModuleNotFoundError: No module named 'future'
>>> foo=math.sqrt
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    foo=math.sqrt
NameError: name 'math' is not defined
>>> import math
>>> foo=math.sqrt
>>> foo(10)
3.1622776601683795
>>> import cmath
>>> cmath.sqrt(-1)
1j
>>> (1+3j)*(9*4j)
(-108+36j)
>>> (1+3j)*(9+4j)
(-3+31j)
>>> 
