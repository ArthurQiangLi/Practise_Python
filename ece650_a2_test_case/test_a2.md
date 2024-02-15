
# Test cases of a2

## The Case in the assignment
```
V 15
E {<2,6>,<2,8>,<2,5>,<6,5>,<5,8>,<6,10>,<10,8>}
s 2 10
V 6
E {<1,3>,<3,2>,<3,4>,<4,5>,<5,2>}
s 5 1
```
Should output
```
2-6-10 
5-2-3-1
```
Note, for first line it could output `2-8-10` too.

## Test1- Check V input

#### [1] Should output: `Error: Set Wrong input for V.` 
```
V 0
```
#### [2] `Error: Set Wrong input for V.`
```
V -100
```

Note: The assignment will not check `'v 0'` or `' v *~!@#$'` or `'V  '` these kinds of syntax, because the professor thinks they are **meaningless** for the goal.


## Test2- Check E input
#### [1] `Error: An edge has same vertces.`
```
V 5
E {<1,1>}
```


#### [2] `Error: Two edges are same/duplicated edges.` 
```
V 5
E {<1,2>, <2,1>}
```
```
V 5
E {<1,2>, <1,2>}
```
#### [3] `Error: Vertex in E not in V.`
```
V 5
E {<1,2>,<5,70>}
```

#### [4] Let Empty E passes
```
V 15
E {}
```
#### [5] But `Error: No path found.` , when hit 's' command:
```
V 15
E {}
s 1 9
``` 

#### [6] `Error: Edge value error.`
```
V 15
E {<-1,2>,<0,6>,<5,6>}
```


## Test3- Check No path found
#### [1] `Error: No path found, no path in the map.`
```
V 5
E {<1,2>,<1,3>,<1,4>}
s 4 5
```
#### [2] `Error: No path found, vertex not exists.`
```
V 5
E {<1,2>, <1,3>, <1,4>}
s 7 100
```
#### [3] `Error: Error search parameter.`
```
V 5
E {<1,2>, <1,3>, <1,4>}
s 7 7
```



## t04 Check Others
#### [1] When new V specification starts, all previous info could be forgotten.
```
V 15
E {<2,6>,<2,8>,<2,5>,<6,5>,<5,8>,<6,10>,<10,8>}
V 5
E {<1,3>,<3,2>,<3,4>,<4,5>,<5,2>}
s 5 1
```
Should output `5-2-3-1`
