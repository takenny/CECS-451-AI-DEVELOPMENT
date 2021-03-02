from mines import Mines


def gen_functions(sweeper, functions):
    functions.clear()
    empty_neighbors = []
    grid = sweeper.checkcell((0, 0))

    # iterate through each row in the grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != '0' and grid[i][j] != ' ':

                # Check neighbors in all directions to see if they are empty
                neighbors = []
                neighbors.clear()
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < len(grid) and 0 <= j+y < len(grid):
                            if grid[i+x][j+y] == ' ':
                                if (i+x, j+y) not in empty_neighbors:
                                    empty_neighbors.append((i+x, j+y))
                                neighbors.append((i+x, j+y))
                # if there is only one neighbor it can be added to the flag list
                if len(neighbors) == int(grid[i][j]):
                    for cord in neighbors:
                        if cord not in sweeper.flags:
                            sweeper.flags.append(cord)
                if len(neighbors) > 0:
                    if grid[i][j] not in functions:
                        functions.update({grid[i][j]: []})
                    functions[grid[i][j]].append(neighbors)
    return empty_neighbors


def get_neighbors(grid, i, j):
    neighbors = []
    neighbors.clear()
    for x in range(-1, 2):
        for y in range(-1, 2):
            if 0 <= i + x < len(grid) and 0 <= j + y < len(grid):
                if grid[i + x][j + y] == ' ':
                    if (i + x, j + y) not in empty_neighbors:
                        empty_neighbors.append((i + x, j + y))
                    neighbors.append((i + x, j + y))



def enumerate_combos(empty_neighbors, sweeper, functions):
    # append to list if true
    safe = []
    listOfStrings = []
    diff = 0

    for i in range(int('1'*len(empty_neighbors), 2)+1):
        binstring = "0" + str(len(empty_neighbors)) + "b"
        binary = format(i, binstring)
        if check_if_true(binary, empty_neighbors, sweeper.flags, functions):
            listOfStrings.append(binary)
    transposed_list = list(map(list, zip(*listOfStrings)))
    for i in range(len(transposed_list)):
        if '1' not in transposed_list[i] and empty_neighbors[i] not in safe:
            safe.append(empty_neighbors[i])

    return safe



def check_if_true(bin_str, neighbors, flags, funct):
    nm = {}
    #print(functions)
    for i in range(len(bin_str)):
        nm.update({neighbors[i]: bin_str[i]})
    for key, value in funct.items():
        for cord_list in value:
            sum = 0
            for cord in cord_list:
                if cord in flags and nm[cord] == 0:
                    return False
                sum += int(nm[cord])
            if sum != int(key):
                return False
    return True


if __name__ == '__main__':
    safe = []
    gridsize = 16
    n_mines = 30
    sweeper = Mines(gridsize, n_mines)
    sweeper.showcurrent()
    functions = {}

    while not sweeper.isfail() and not sweeper.checkmines():
        print(sweeper.isfail(), sweeper.checkmines())
        print("starting gen functions")
        empty_neighbors = gen_functions(sweeper, functions)
        print(empty_neighbors)
        print("end gen functions")
        print("start enumerate")
        safe = enumerate_combos(empty_neighbors, sweeper, functions)
        print("end enumerate")

        for cell in safe:
            sweeper.checkcell(cell)
            sweeper.showcurrent()
        print("safe:", len(safe), "flags:", len(sweeper.flags))
