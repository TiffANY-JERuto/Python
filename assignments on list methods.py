Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> print(cars[1])
Ford
>>> print(cars)
['Jeep', 'Ford', 'Toyota', 'Mazda', 'Honda', 'Hyundai']
>>> 
>>> 
>>> 
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> cars[2] = "Kia"
>>> print(cars)
['Jeep', 'Ford', 'Kia', 'Mazda', 'Honda', 'Hyundai']
>>> 
>>> 
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> for x in cars:
	print(x)

	
Jeep
Ford
Toyota
Mazda
Honda
Hyundai
>>> 
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> if "Honda" in cars:
	print("Definitely 'Honda' is in this list")

	
Definitely 'Honda' is in this list
>>> 
>>> 
>>> 
>>> 
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> print(len(cars))
6
>>> 
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> cars.append("Volkswagen")
>>> print(cars)
['Jeep', 'Ford', 'Toyota', 'Mazda', 'Honda', 'Hyundai', 'Volkswagen']
>>> 
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> cars.remove("Ford")
>>> print(cars)
['Jeep', 'Toyota', 'Mazda', 'Honda', 'Hyundai']
>>> 
cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> cars.pop()
'Hyundai'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> countries = list(("apple", "banana", "cherry"))
>>> print(countries)
['apple', 'banana', 'cherry']
>>> countries.clear
<built-in method clear of list object at 0x0347D738>
>>> 
>>> countries = list(("Namibia", "Kenya", "Zanzibar"))
>>> print(countries)
['Namibia', 'Kenya', 'Zanzibar']
>>> cars = ["Jeep", "Ford", "Toyota", "Mazda", "Honda", "Hyundai"]
>>> 
>>> cars.reverse("cars")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    cars.reverse("cars")
TypeError: reverse() takes no arguments (1 given)
>>> cars.sort()
>>> cars
['Ford', 'Honda', 'Hyundai', 'Jeep', 'Mazda', 'Toyota']
>>> 
>>> cars.reverse()
>>> cars
['Toyota', 'Mazda', 'Jeep', 'Hyundai', 'Honda', 'Ford']
>>> cars.index()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    cars.index()
TypeError: index() takes at least 1 argument (0 given)
>>> 
>>> 
>>> x = [0, 1,2, 3, 4, 5, 6, 7, 8, 9]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> y=[k*10 for k in x]
>>> y
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> 
>>> 
>>> for k in x
SyntaxError: invalid syntax
>>> for k in y
SyntaxError: invalid syntax
>>> for k in x:
	print(k)

	
0
1
2
3
4
5
6
7
8
9
>>> k = x[0:5]
>>> k
[0, 1, 2, 3, 4]
>>> v = [6:10]
SyntaxError: invalid syntax
>>> v
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> v = x[6:10]
>>> v
[6, 7, 8, 9]
>>> v = x[6:11]
>>> v
[6, 7, 8, 9]
>>> v = x[6:12]
>>> v
[6, 7, 8, 9]
>>> v = x[5:12]
>>> v
[5, 6, 7, 8, 9]
>>> 
>>> n = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
>>> n
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> 
>>> m = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print(m)
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> 
