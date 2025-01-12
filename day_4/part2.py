def main():
    with open("problem4.txt") as f:
        file = f.read().splitlines()

    result = 0
    row_len = len(file[0])
    height_len = len(file)   
    
    for _ in range(height_len - 2):
        start = 0
        end = 3
        
        for i in range(row_len - 2):
            matrix = get_matrix_3_by_3(file, start, end)
            if check_x_mas(matrix):
                result += 1
            start += 1 
            end += 1
        
        del file[0]
    
    print(result)

def get_matrix_3_by_3(file, start, end):
    result = []
    
    for i, line in enumerate(file):
        result.append(line[start:end])
        if i == 2:
            break
    return result

def check_x_mas(matrix):
    first, second, third = matrix[0], matrix[1], matrix[2]
    left_word = first[0] + second[1] + third[2]
    right_word = first[2] + second[1] + third[0]
    
    left = left_word in ("MAS", "SAM")
    right = right_word in ("MAS", "SAM")

    return (left and right)
    
if __name__ == "__main__":
    main()