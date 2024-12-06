## Part 1 :star:
[part1.py](part1.py) <br><br>
We are getting input as:
```
3   4
4   3
2   5
1   3
3   9
3   3
```
We need to check how far apart 2 smallest numbers are.
So we are taking smallest number from right and smallest from right etc. and we need to calculate what is the distance between those 2 numbers.
<br>
After that we need to calculate finall result by adding those distances. 
<br><br>
Pretty easy problem at the start. 
<br><br>
**Steps to solve**
1. Create 2 arrays
2. Add to one arrays numbers from first column. Exacly the same for second column. 
3. Sort them that they will be increasing.
4. Change difference between 2 numbers. One from first list and the other from another one.
5. Every time we will get diff value add it to some counter variable.
6. There you go :)


## Part 2 :star:
[part2.py](part2.py) <br><br>
We getting same input as before, but now the task is different.
We need to check how many times number from first list appears in second one. If we know that for example 3 appears 4 times in antoher list **we will multiply 3 * 4 = 12**.
<br><br>
**Steps to solve**
1. Create 2 arrays
2. Add to one arrays numbers from first column. Exacly the same for second column. 
3. Sort them that they will be increasing.
4.Check for each number how many times in another list the number is appearing. 
5. Multiply the value.
6. Add value to result 
7. Repeat to the end of the first array.

