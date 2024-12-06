def main():
    safe_reports = 0
    with open("problem2.txt") as f:
        for line in f:
            numbers = line.split(" ")
            numbers = [int(number.rstrip("\n")) for number in numbers]

            for i in range(len(numbers)):
                copy_numbers = numbers.copy()
                del copy_numbers[i]
                report = check_report(copy_numbers)
                if report:
                    safe_reports += 1
                    break

    print(safe_reports)

def check_report(numbers):
    increase = numbers[0] < numbers[1]
    current_number = numbers[0]
    for i in range(1, len(numbers)):
        if not (1 <= abs(abs(current_number)  - abs(numbers[i])) <= 3):
            return False
        elif increase and current_number > numbers[i]:
            return False
        elif not increase and current_number < numbers[i]:
            return False
        
        current_number = numbers[i]
    
    return True

if __name__ == "__main__":
    main()