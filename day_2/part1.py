safe_reports = 0

with open("problem2.txt") as f:
    for line in f:
        numbers = line.split(" ")
        numbers = [int(number.rstrip("\n")) for number in numbers]

        increase = numbers[0] < numbers[1]
        current_number = numbers[0]
        flag = True
        for i in range(1, len(numbers)):
            #print(abs(abs(current_number)  - abs(numbers[i])))
            if not (1 <= abs(abs(current_number)  - abs(numbers[i])) <= 3):
                flag = False
                break
                
            if increase and current_number > numbers[i]:
                flag = False
                break

            elif not increase and current_number < numbers[i]:
                flag = False
                break
            
            current_number = numbers[i]

        if flag:
            safe_reports += 1

    print(safe_reports)
