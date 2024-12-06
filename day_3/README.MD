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
