def main():
    safe_reports = 0
    with open("problem2.txt") as f:
        for line in f:
            numbers = line.split(" ")
            numbers = [int(number.rstrip("\n")) for number in numbers]

            report = check_levels(numbers)
            if report:
                safe_reports += 1

    print(safe_reports)

def check_levels(numbers, wrong_index=None):
    cp_numbers = numbers
    if wrong_index: 
        del numbers[wrong_index]

    increase = numbers[0] < numbers[1]
    current_number = numbers[0]
    for i in range(1, len(numbers)):
        if not (1 <= abs(abs(current_number)  - abs(numbers[i])) <= 3):
            if not wrong_index:
                return check_levels(cp_numbers, i)
            return False
        elif increase and current_number > numbers[i]:
            if not wrong_index:
                return check_levels(cp_numbers, i)
            return False
        elif not increase and current_number < numbers[i]:
            if not wrong_index:
                return check_levels(cp_numbers, i)
            return False
        
        current_number = numbers[i]
    
    return True

if __name__ == "__main__":
    main()