## Part 1 :star:
[part1.py](part1.py) <br><br>
This problem wasn't that hard.
Main things to check in any 'report':
- If the whole array is constantly increasing or decresing
- If every next value differ from the previous by at least 1 and at most 3. 

So after checking those 2 values by if's statements we can acknowledge if the 'report' is safe or unsafe.

## Part 2 :star:
[part2.py](part2.py) <br><br>

This problem expanding first part.<br>
Addiotional things to consider: 
- Every 'report' will tolerate one bad 'level'

To solve the problem I modified code from previous part.
**What's happening in the code?**
<br>
We are checking same 'report' but without one 'level' with every (one by one)'level' deleted. If the function return True we now that at least of those permutations will be correct. 
