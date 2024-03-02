def get_triangle(rows: int):
    List = []
    for i in range(rows):
        line = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                line[j] = List[i - 1][j - 1] + List[i - 1][j]
        List.append(line)
    for i in range(len(List)):
        print(List[i], end='\n')
    return List


def formatting(rows: int):
    List = []

    for i in range(rows):
        line = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                line[j] = List[i - 1][j - 1] + List[i - 1][j]
        List.append(line)

    for i in range(rows):
        for j in range(rows-i-1):
            print(format(" ", "<1"), end="")
        for j in range(i+1):
            print(format(List[i][j], "<2"), end="")
        print()

    return List


get_triangle(5)
formatting(5)
