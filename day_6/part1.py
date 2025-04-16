class Game:
    def __init__(self, file):
        self.file = [line.strip("\n") for line in file]
        self.direction = "up"
        self.line, self.index = self.get_starting_position(file)

    def get_starting_position(self, file):
        line_counter = 0
        for line in file:
            index = 0
            for char in line:
                if char == "^":
                    return line_counter, index
                index += 1
            line_counter += 1
    
    def change_direction(self):
        directions = ["up", "right", "down", "left"]
        index = directions.index(self.direction)
        if index + 1 == 4:
            self.direction = directions[index]
            return
        self.direction = directions[index+1]

    def move_up(self):
        # check if the char above spaceship is a object
        if self.file[self.current_position[0]][self.current_position[1]] == "#":
            self.change_direction()
        else:
            self.file[self.current_position[0]][self.current_position[1]] = "X"
            self.current_position = self.current_position[0] - 1, self.current_position[1]
         



def main():
    with open("test1.txt") as f:
        file = f.readlines()

    game = Game(file)

    while True:
        if game.direction == "up":
            game.move_up()
            print(game.direction)

if __name__ == "__main__":
    main()