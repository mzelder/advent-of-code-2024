## Part 1 :star:
[part1.cs](part1/Program.cs) <br><br>
 Our input looks like this 
 ```
 ....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

**Main problem to solve:**<br>
In the first part we need to check how many moves was made by a spaceship - `^`. Spaceship have very easy to understand rule - if he have object - `#` 
in front of him then he will turn right.

## Solving
We upload whole input into the list where each element (line) have his own array `char[]`.<br>
Also at the start we need to fing out where exacly our spaceship and this is why wrote funcion `findStartingPosition()` to check what is the "row" and "column" and I added those informations into tuple where `line` is a row and `index` is a colum. <br>
With those informations we can start checking if char before our spaceship is a `#`-object. <br>
Four functions for moving up,down etc. are pretty self explanatory :) <br>
Each time the spaceship will made move we will mark location as `X` so we later can count how many move spaceship made. 

## Part 2 :star:
[part2.py](part2.py) <br><br>
