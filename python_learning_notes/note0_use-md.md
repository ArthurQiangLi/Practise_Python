# 1. h1 Texts [I learned from this video](https://www.youtube.com/watch?v=bTVIMt3XllM)
## h2 Markdown note tools: Bear app, Joplin, standard Notes, Obsidian
### h3 Markdown blog tool: ghost
#### h4
##### h5
default text size 123
###### h6

[link text in blue](http://github.com)

**bolded text** *Italied test* use <br> 

'\<br>' for breaking

 ~~strikethrough text~~ 
 
 `inline code` 

==Hightlights useing '=='== <mark>Highlights</mark>

X<sub>the sub</sub>    |   X<sup>the sup</sup>

```py
import system
def add(a):
    a = 2
class Example(system):
    for code ,segment in range(10):
    multipule += 'lines'
```
# 2. context structs (list, table)
1. numbered list
2. automatic added by 'markdown all in one' extension

---
    what ever
    1. becomes code segment if indented
    2. must be at least 2 lines
    3. ...

---
**Dotlist**
- dot list
  - what ever
- another item

---
| name | age | balence |
|:----| ----:| ----|
|left | right | center |
| arthur | 17| $500B |

| one column |
| ---| 
| how to use Latex|
| can also insert a picture in a table |




# 2. local hyper link

this is a link : [link text](#1-advanced-table) to #1. advanced: tables

# 3. hidden details block
<details>
    <summary> Show Hidden info with a click </summary>
    what is not showed by default, 
</details>


# 3. Advanced topic: using LaTex

> Example below, start with '$' for inline ones or '$$' for paragraphs.

**Line-line Intersection**
(From [Wikipedia](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection))

Given two lines $L_1$ and $L_2$, where the line $L_1$ is defined by two distinct points $(x_1, y_1)$ and $(x_2, y_2)$, and the line $L_2$ is defined by two distinct points $(x_3, y_3)$ and $(x_4, y_4)$. Their intersection (if defined) is a point $(P_x, P_y)$ defined by the following equations:
$$
\begin{array}{lcl}
P_x &=& \frac{(x_1y_2 - y_1x_2)(x_3 - x_4) - (x_1 - x_2)(x_3y_4 - y_3x_4)}{(x_1 - x_2)(y_3 - y_4) - (y_1 - y_2)(x_3 - x_4)}\\[.2in]
P_y &=& \frac{(x_1y_2 - y_1x_2)(y_3 - y_4) - (y_1 - y_2)(x_3y_4 - y_3x_4)}{(x_1 - x_2)(y_3 - y_4) - (y_1 - y_2)(x_3 - x_4)}
\end{array}
$$

__Note: these equations do not handle special cases, such as when the lines are parallel ...__