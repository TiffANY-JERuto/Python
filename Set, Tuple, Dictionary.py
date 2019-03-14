Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = (1, 2, 3, 4, 5)
>>> a.append(6)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.append(6)
AttributeError: 'tuple' object has no attribute 'append'

>>> x.pop()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.pop()
NameError: name 'x' is not defined
>>> x.remove()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.remove()
NameError: name 'x' is not defined
>>> x.sort()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.sort()
NameError: name 'x' is not defined
>>> x.extend(6, 7, 8, 9,)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.extend(6, 7, 8, 9,)
NameError: name 'x' is not defined
>>> a.sum()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.sum()
AttributeError: 'tuple' object has no attribute 'sum'
>>> a.extend(6, 7, 8, 9,)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.extend(6, 7, 8, 9,)
AttributeError: 'tuple' object has no attribute 'extend'
>>> a.index(5)
4
>>> len(a)
5
>>> for y in a:
	print (y*10)

	
10
20
30
40
50
>>> y = (6, 7, 8, 9,)
>>> z = y + x
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    z = y + x
NameError: name 'x' is not defined
>>> y = (6, 7, 8, 9)z = y + x
SyntaxError: invalid syntax
>>> y = (6, 7, 8, 9)
>>> z= y+a
>>> 
>>> z
(6, 7, 8, 9, 1, 2, 3, 4, 5)
>>> 
>>> 5 in a
True
>>> 7 in a
False
>>> a*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
>>> y*10
(6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9)
>>> 
>>> b= set([1, 2, 3, 1, 1, 2, 4, 5, 4])
>>> b
{1, 2, 3, 4, 5}
>>> 
>>> c ={3, 3, 4, 5, 6, 5, 4, 6, 7,}
>>> c
{3, 4, 5, 6, 7}
>>> b.add(6)
>>> b
{1, 2, 3, 4, 5, 6}
>>> c.add(8)
>>> c
{3, 4, 5, 6, 7, 8}
>>> b.remove (4)
>>> b
{1, 2, 3, 5, 6}
>>> b.update(10,11)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    b.update(10,11)
TypeError: 'int' object is not iterable
>>> c.update(10, 11)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    c.update(10, 11)
TypeError: 'int' object is not iterable
>>> 
>>> 
>>> b.remove(0)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    b.remove(0)
KeyError: 0
>>> b.discard(9)
>>> c.discard(9)
>>> 
>>> c
{3, 4, 5, 6, 7, 8}
>>> b.difference(c)
{1, 2}
>>> c.difference(b)
{8, 4, 7}
>>>  b.add(6, 7, 8, 9, 10, 11, 12, 13, 14)
SyntaxError: unexpected indent
>>> b
{1, 2, 3, 5, 6}
>>> b.add(7)
>>> b
{1, 2, 3, 5, 6, 7}
>>> c
{3, 4, 5, 6, 7, 8}
>>> c.add(10)
>>> c
{3, 4, 5, 6, 7, 8, 10}
>>> c.difference in (b)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    c.difference in (b)
TypeError: unhashable type: 'set'
>>> b.difference in (c)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    b.difference in (c)
TypeError: unhashable type: 'set'
>>> c.difference(b)
{8, 10, 4}
>>> b.difference(c)
{1, 2}
>>> 
>>> c.intersection(b)
{3, 5, 6, 7}
>>> b.intersection(a)
{1, 2, 3, 5}
>>> b.union(c)
{1, 2, 3, 4, 5, 6, 7, 8, 10}
>>> 
>>> 
>>> 
>>> codes={"Kenya": 254, "Uganda": 256, "Tanzania": 255}
>>> codes
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255}
>>> codes["Kenya"]
254
>>> codes["Uganda"]
256
>>> codes["Tanzania"]
255
>>> codes["Rwanda"]=250
>>> codes
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250}
>>> codes["Kenya"]=1000
>>> codes
{'Kenya': 1000, 'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250}
>>> codes["Kenya"]=254
>>> codes
{'Kenya': 254, 'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250}
>>> "Kenya" in codes
True
>>> "KENYA" in codes
False
>>> codes.keys()
dict_keys(['Kenya', 'Uganda', 'Tanzania', 'Rwanda'])
>>> codes.values()
dict_values([254, 256, 255, 250])
>>> for key in codes.keys():
	print(key)

	
Kenya
Uganda
Tanzania
Rwanda
>>> for value in codes.values()
SyntaxError: invalid syntax
>>> for value in codes.values():
	print(values)

	
Traceback (most recent call last):
  File "<pyshell#87>", line 2, in <module>
    print(values)
NameError: name 'values' is not defined
>>> for value in codes.values():
	print(value)

	
254
256
255
250
>>> codes.pop("Kenya")
254
>>> codes
{'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250}
>>> codes["Burundi"]= 251
>>> codes
{'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250, 'Burundi': 251}
>>> codes["Ghana"] = 259
>>> codes
{'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250, 'Burundi': 251, 'Ghana': 259}
>>> codes["Nigeria"] = 288
>>> codes["Bangkok"] = 34
>>> codes["Europe"] = 78
>>> codes
{'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250, 'Burundi': 251, 'Ghana': 259, 'Nigeria': 288, 'Bangkok': 34, 'Europe': 78}
>>> codes["Netherlands]
	  
SyntaxError: EOL while scanning string literal
>>> codes["Netherlands"] = 22
	  
>>> codes["Canada"] = 77
	  
>>> codes
	  
{'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250, 'Burundi': 251, 'Ghana': 259, 'Nigeria': 288, 'Bangkok': 34, 'Europe': 78, 'Netherlands': 22, 'Canada': 77}
>>> codes["Ghana"]
	  
259
>>> codes["Bangkok"]
	  
34
>>> codes["Netherlands"]
	  
22
>>> codes["Canada"]
	  
77
>>> codes.pop["Burundi"]
	  
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    codes.pop["Burundi"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> codes.pop("Burundi")
	  
251
>>> codes
	  
{'Uganda': 256, 'Tanzania': 255, 'Rwanda': 250, 'Ghana': 259, 'Nigeria': 288, 'Bangkok': 34, 'Europe': 78, 'Netherlands': 22, 'Canada': 77}
>>> type(codes)
	  
<class 'dict'>
>>> squares=dict()
	  
>>> type(squares)
	  
<class 'dict'>
>>> squares[1]=1
	  
>>> squares[2]=2
	  
>>> squares[2]=2squares[1]=1
	  
SyntaxError: invalid syntax
>>> 
	  
>>> 
	  
>>> squares[1]
	  
1
>>> squares[2]
	  
2
>>> squares[1]=1
	  
>>> sqaures[2]=4
	  
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    sqaures[2]=4
NameError: name 'sqaures' is not defined
>>> squares[2]=4
	  
>>> squares[3]=9
	  
>>> sqaures[4]=16
	  
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    sqaures[4]=16
NameError: name 'sqaures' is not defined
>>> squares[4]=16
	  
>>> cubes = dict()
	  
>>> numbers= range(0,10)
	  
>>> for number in numbers:
	  cubes [number] = number*number*number

	  
>>> cubes
	  
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> tens = dict ()
	  
>>> numbers= range(0,10)
	  
>>> for number in numbers:
	  tens[number] = number*10

	  
>>> tens
	  
{0: 0, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}
>>> fourth = dict ()
	  
>>> numbers= range(49,59)
	  
>>> for number in numbers:
	  fourth[number] = numbers%3

	  
Traceback (most recent call last):
  File "<pyshell#143>", line 2, in <module>
    fourth[number] = numbers%3
TypeError: unsupported operand type(s) for %: 'range' and 'int'
>>> fourth
	  
{}
>>> for number in numbers:
	  fourth[number] = number%3

	  
>>> fourth
	  
{49: 1, 50: 2, 51: 0, 52: 1, 53: 2, 54: 0, 55: 1, 56: 2, 57: 0, 58: 1}
>>> 
