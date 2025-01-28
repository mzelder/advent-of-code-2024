## Part 1 :star:
[part1.py](part1.py) <br><br>
Our input looks like this: <br>
```
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```
**Main problem to solve:** <br>
First part where numbers are setup like this: `47|13` are the rules. That are telling that number `47` need to be before number `13` in the sequcne of numbers like this `75,47,61,53,29`. But number `13` doesn't need to be immediately after first number. 
<br><br>
If all the rules for the "row numbers" are okay then we are taking middle number so in this example it will be `61` if all rules are correct.
<br><br>

## Solving
**This is how i solved the problem:**
1. Split input into 2 arrays. One with all rules and second with all sequence of numbers.
2. Check one by one if the rules are correct.
3. This code should be self-explanotary.<br>
```
# ex. 97|13 not true here so we are not counting it
if first > second and row.index(first) > row.index(second):
    return 0
# ex. 47|53 not rue here so we are not counting it
elif first < second and row.index(first) > row.index(second): 
    return 0
```
3. If all the rules are correct then we will take middle number from the row and add it to the result.
4. Print result. 

## Part 2 :star:
[part2.py](part2.py) <br><br>
