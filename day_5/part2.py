from part1 import split_input

def check_rules(row, rules):
    print(row)
    for rule in rules:
        first, second = rule[0], rule[1]
        try:
            first_idx, second_idx = row.index(first), row.index(second)
            # ex. 97|13 not true here so we are not counting it
            if first > second and first_idx > second_idx:
                print("here")
                row[first_idx] = second
                row[second_idx] = first
            # ex. 47|53 not rue here so we are not counting it
            elif first < second and first_idx > second_idx:
                print("here1")
                row[first_idx] = second
                row[second_idx] = first
        except ValueError:
            continue
    
    print(row)
    return row[len(row) // 2 ]

def main():
    result = 0
    rules, page_numbers = split_input("test.txt")
    result1 = check_rules(page_numbers[0], rules)
    print(result1)
    # for row in page_numbers:
    #     result += check_rules(row, rules)

    #print(result)



if __name__ == "__main__":
    main()