import re
from typing import List

result = 0

def main():
    with open("problem4.txt") as f:
        file = f.read().splitlines()

    line_lenght = len(file[0])

    # vertical check and vertical backward check
    vertical_check(file)

    # horizontal check and horizontal backward check
    # transpose input (like a matrix) 
    horizontal_check(file, line_lenght)

    # diagonal check (left top, right down) and backwards
    diagonal_check_left_to_right(file, line_lenght)

    # diagonal check (right top, left down) and backwards
    diagonal_check_right_to_left(file, line_lenght)

    print(result)

def search_for_XMAS(lines: List[str]) -> None: 
    global result
    for line in lines:---
        backward_line = line[::-1]
        result += len(re.findall(r"XMAS", line))
        result += len(re.findall(r"XMAS", backward_line))

def vertical_check(file):
    search_for_XMAS(file)

def horizontal_check(file, line_lenght):
    array = []
    for i in range(line_lenght):
        for line in file:
            array.append("")
            array[i] += line[i]

    transposed_input = "\n".join(array).rstrip()
    transposed_lines = transposed_input.split("\n")
    search_for_XMAS(transposed_lines)

def diagonal_check_left_to_right(file, line_lenght):
    array1 = []
    for i in range(line_lenght):
        array1.append("")
        for j in range(line_lenght - i):
            array1[i] += file[j][j+i]
    
    array2 = []
    for i in range(1, line_lenght):
        array2.append("")
        for j in range(line_lenght - i):
            array2[i-1] += file[j+i][j]
 
    combined_arrays = array1 + array2
    search_for_XMAS(combined_arrays)

def diagonal_check_right_to_left(file, line_lenght):
    array1 = []
    for i in range(line_lenght):
        array1.append("")
        for j in range(line_lenght - i):
            array1[i] += file[j][line_lenght - j - 1 - i]

    array2 = []
    for i in range(1, line_lenght):
        array2.append("")
        for j in range(line_lenght - i):
            array2[i-1] += file[j+i][line_lenght - j - 1]

    combined_arrays = array1 + array2
    search_for_XMAS(combined_arrays)

if __name__ == "__main__":
    main()