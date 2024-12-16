import re

result = 0

def main():
    with open("test2.txt") as f:
        file = f.read().splitlines()

    line_length = len(file[0])
    i = 0
    j = 3
    array = []
    while i < len(file) - 2:
        array.append([])
        while j < line_length:
            three_grid_array = []
            three_grid_array.append(file[i][j-3:j])
            three_grid_array.append(file[i+1][j-3:j])
            three_grid_array.append(file[i+2][j-3:j])
            print(three_grid_array)
            array[i].append(three_grid_array)
            j += 1
        i += 1
    
    print(array)
def find_matching_words():
    pass 

if __name__ == "__main__":
    main()