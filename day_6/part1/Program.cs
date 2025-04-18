List<char[]> lines = new List<char[]>();
using (StreamReader sr = new StreamReader("problem6.txt")) {
    string? line;
    while ((line = sr.ReadLine()) != null) {
        lines.Add(line.ToCharArray());
    }
}

(int line, int index) currentPosition = findStartingPosition();
int direction = 1; // 0 left, 2 right, 1 up, 3 down;

try
{
    while (true)
    {
        switch (direction)
        {
            case 0:
                moveLeft();
                break;
            case 1:
                moveUp();
                break;
            case 2:
                moveRight();
                break;
            case 3:
                moveDown();
                break;
        }
    }
} catch (Exception e)
{
    int madeMoves = 1;
    foreach (var line in lines)
    {
        foreach (var c in line)
        {
            if (c == 'X') madeMoves++;
        }
    }
    Console.WriteLine(madeMoves);

}

(int, int) findStartingPosition()
{
    int line = 0;
    int index = 0;
    char currentChar;
    char[] currentStr;
    char desireChar = '^';

    while (line != lines.Count)
    {
        currentStr = lines[line];
        while (index != currentStr.Length)
        {
            if ((currentChar = currentStr[index]) == desireChar)
            {
                return (line, index);
            }
            index++;
        }
        index = 0;
        line++;
    }

    return (line, index);
}

void moveUp()
{
    while (true)
    {
        int aboveChar = lines[currentPosition.line - 1][currentPosition.index];
        if (aboveChar != '#') // Check if char above ship is #, if not then move up 
        {
            lines[currentPosition.line][currentPosition.index] = 'X';
            currentPosition.line--;
            direction = 2;
        } else
        {
            break;
        }
    }
}

void moveDown()
{
    while (true)
    {
        int underChar = lines[currentPosition.line + 1][currentPosition.index];
        if (underChar != '#') // Check if char under ship is #, if not then move up 
        {
            lines[currentPosition.line][currentPosition.index] = 'X';
            currentPosition.line++;
            direction = 0;
        }
        else
        {
            break;
        }
    }
}

void moveLeft()
{
    while (true)
    {
        int leftChar= lines[currentPosition.line][currentPosition.index - 1];
        if (leftChar != '#') // Check if char on the left side ship is #, if not then move up 
        {
            lines[currentPosition.line][currentPosition.index] = 'X';
            currentPosition.index--;
            direction = 1;
        }
        else
        {
            break;
        }
    }
}

void moveRight()
{
    while (true)
    {
        int rightChar = lines[currentPosition.line][currentPosition.index + 1];
        if (rightChar != '#') // Check if char on the right side ship is #, if not then move up 
        {
            lines[currentPosition.line][currentPosition.index] = 'X';
            currentPosition.index++;
            direction = 3;
        }
        else
        {
            break;
        }
    }
}