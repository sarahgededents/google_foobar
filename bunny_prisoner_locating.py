def cell(x, y):
    return str(sum(range(x+y)) - y + 1)


def print_cells(size): #print inc numbers triangle representation
    for j in reversed(range(1, size)):
        for i in range(1, size - j):
            print(cell(i, j), end=' ')
        print()