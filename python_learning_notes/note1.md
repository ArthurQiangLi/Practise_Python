# Notes when reading <br>[Python Crash Course, Eric Matthes]

# #1 2024, Jan 28
```py
1. sort.upper(), sort.title(), sort.lower()
2. '+'
3. str.rstrip() remove spaces
4. str.lstrip()  str.strip()  str(18) -> '18'
5. #comment and '''comment lines'''
6. import this --> the Zen of Python
7. somelist = ['trek', 9, [a,b,c], 18] or []for new a empty list
    1. somelist[0] -> first item
    2. somelist[-1] -> last item, -2 -> second last
    3. ls.append('item') -> add item
    4. ls.insert(0, item)  -> insert in indexed position
    5. de ls[0]  -> delete one item
    6. poped_item = ls.pop() -> pop last(return and del) 
        1. pop(i) -> pop the specified one
    7. ls.remove(item) -> remove by value (for the first found one)
8. ls.sort(reverse=True) -> sort by alphabeta or not
9. reverse(ls) -> reverse item orders in a list
10. len(ls) -> size of a ls
```
# #2 2024, Jan 28
```py

1. for value in range(5) ->    <5 from 0~4, excluding 5, total cnt = 5
2. for value in range(1,5) -> 1,2,3,4, <5 too
3. list(range(1,6)) -> get a new list [1,2,3,4,5]
4. list(range(2,11,2)) -> from 2 < 11 every 2 : [2,4,6,8.10]
5. list = [1,2,....] , min(ls) , max(ls), sum(ls)
6. squares = [v**2 for v in range(1,11)]  -> [1,4,9,...100]
7. plays[0:3] ->0,1,2 items, form a sub-list
   1. ls[:4] -> first to 4th
   2. ls[2:] ->[2] to last
   3. [-3:] -> last 3 items
8. ls1 = ls2[:] -> this is the hard copy, ls1=ls2 is reference copy
9. **tuple**: tup1 = (200,50), x=tup1[0], tuples can only be defined and **redefined**, not be modified.
10. if (age > 21) and (age < 28):
11. if a in b,  if a not in b
12. if ls1 -> check if ls1 is empty
```

# #3
```py
1. **Dictionary** alien0 = {'color':'g',  'point':5} --> key-value pair, both key and value can be anything: number, string, list and dictionary,,,
2. print(alien0['point'])  -> 5
3. alien0 = {} -> an empty dict
4. del alien0['point'] -> delete an item
5. for k,v in dict.items():
   1. for k in dict.keys():  --> here dict.keys() is actually a list object
   2. for v in dict.value():
   3. ls = set(ls) -> return the list, all items are **identical**
6. def foo():
7. foo(ls[:]) --> pass a list to a function, here create a new copy of the list, not a reference,
8. def make_pizze(size, *topings)  --> where *topings is a tuple (a,b,c,d,...)
9. def build_profile(first, last, **user_info) -> where **user_info is to new an empty dict

```


# #4
```py
1. import pizza  -> pizza is a file name, also is called 'module name'
2. from module_name import funct_name as
   1. from module_name import fun1, fun2, fun3
   2. from car import Car, ElectricaCar -> import class, class name is usually **Cameled**
   3. import module_name as mn
   4. import car -> is to import car.py module/file
   5. from collections import OrderedDict -> standard lib
3. class Dog():
4. class ElectricCar(Car) -> Car is the superclass
5. with open('a.txt') as fileobject:
   1. contents = fileobject.read()
   2. or for line in fileobject:
      1. ....
6. with open(filename, 'w') as file object:  -> 'w' will create or cover files with same name, 'a' will append content in the end of the file
   1. fileobject.write("xxxx")
```


# #5
```py
1. try:
2. except ZeroDivisionError:
   1. pass -> do nothing
3. else:
   1. do other things
4. int(5)/int(2) = 2.5 
5. TestCase is a set of unittest
6. class NameTestCase(unittest.TestCase):  -> you must super the TextCase class
7. test_fun1:  --> function name must starts with 'test_'
    - assertEqual(a,b) -> check equal, also NotEqual
    - assertIn(item, list) -> check belong, also NotIn
    - assertTure(x)  -> check true, also False
```