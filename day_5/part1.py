def split_input(file_name):
    # split to 2 arrays 
    # rules with the actuall rules 
    # page_numbers with the seq of the page numbers 
    with open(file_name) as f:
        file = f.readlines()
    
    file = [line.strip("\n") for line in file]
    rules = []
    page_numbers = []
    for line in file:
        if "|" in line:
            number1, number2 = line.split("|")
            rules.append([int(number1), int(number2)])
        elif "," in line:
            numbers = line.split(",")
            numbers = [int(x) for x in numbers]
            page_numbers.append(numbers)
    
    return rules, page_numbers


def check_rules(row, rules):
    for rule in rules:
        first, second = rule[0], rule[1]
        try:
            # ex. 97|13 not true here so we are not counting it
            if first > second and row.index(first) > row.index(second):
                return 0
            # ex. 47|53 not rue here so we are not counting it
            elif first < second and row.index(first) > row.index(second): 
                return 0
        except ValueError:
            continue
    
    return row[len(row) // 2 ]


def main(): 
    result = 0
    
    rules, page_numbers = split_input("problem5.txt")

    for row in page_numbers:
        result += check_rules(row, rules)
    
    print(result)

if __name__ == "__main__":
    main()