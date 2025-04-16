List<string> lines = new List<string>();
using (StreamReader sr = new StreamReader("../test1.txt")) {
    string? line;
    while ((line = sr.ReadLine()) != null) {
        lines.Add(line);
    }
}
(int line, int index) currentPosition = findStartingPosition();
int direction = 1; // 0 left, 2 right, 1 up, 3 down;

(int, int) findStartingPosition() {
    int line = 0;
    int index = 0;
    char currentChar;
    string currentStr;
    char desireChar = '^';

    while (line != lines.Count) {
        currentStr = lines[line];
        while (index != currentStr.Length) {
            if ((currentChar = currentStr[index]) == desireChar) {
                return (line, index);
            }
            index++;
        }
        index = 0; 
        line++;
    }

    return (line, index);
}

void moveUP() {
    while (true) {
        
    }
}