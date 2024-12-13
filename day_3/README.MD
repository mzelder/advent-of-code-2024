## Part 1 :star:
[part1.py](part1.py) <br><br>
We getting input like this: ```xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))```
<br>
To solve the problem we need to find uncorrupted memories that looks like this: ```mul(x,y)``` and after finding we need to multiply ```x * y```. <br>
Result will be sum of values from multiplication.
<br><br>
**Steps to solve**
1. Load input to app
2. Use [regex](https://en.wikipedia.org/wiki/Regular_expression) for checking patterns.
3. Get data from mul() string. 
4. Multiply values from mul().
5. Add multiplied values to result value.  

## Part 2 :star:
[part2.py](part2.py) <br><br>
The second part of the problem is a little bit harder.<br>
The additional problem is that also in input text we are getting do's and don'ts functions.  
```xmul(2,4)&mul[3,7]!^don't()_mul(5,5)**do()**```
<br>
<br>
Everything after don'ts() functions should be skipped and after do's() functions executed.  
<br>
**My aproach to solve the problem**
1. Try to find indexes of mul(x, y) using [regex](https://en.wikipedia.org/wiki/Regular_expression).
2. Try to find indexes of do() and don't() functions using [regex](https://en.wikipedia.org/wiki/Regular_expression).
3. Connect 2 arrays in one so later we can iterrate through this. 
4. Sort the main array so we will know if the do or don't function is before mul(x,y) function.
5. Iterrate through the main array. 
    - via the start and end index touple we can find actuall words 
    - then we will check if the word if equal to do, if so we will change **operation** variable to True (any "flag" variable is okey)
    - if its actuall mul(x, y) funciton the we will multiply it like in first part we need to check if **operation** is set to **True** or **False** (if it's a do() or don't() function), if so multiply and add to result. 
    - otherwise the **operation** will be changed to **False** becuase we know that there it's only `do()`, `mul(x, y)` and `dont()`
6. Print the result and we can get our answer.
