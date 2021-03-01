from mines import Mines


def gen_functions(sweeper, grid, functions):
    functions.clear()
    empty_neighbors = []

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
                if len(neighbors) == 1 and neighbors[0] not in sweeper.flags:
                    sweeper.flags.append(neighbors[0])
                # if there are
                elif len(neighbors) > 1:
                    if grid[i][j] not in functions:
                        functions.update({grid[i][j]: []})
                    functions[grid[i][j]].append(neighbors)
    return empty_neighbors


def enumerate_combos(empty_neighbors):
    # append to list if true
    listOfStrings = []
    diff = 0

    for i in range(int('1'*len(empty_neighbors), 2)+1):
        binstring = "0" + str(len(empty_neighbors)) + "b"
        binary = format(i, binstring)
        listOfStrings.append(binary)
    print(listOfStrings)


def check_if_true(bin_str, neighbors, flags, funct):
    nm = {}
    for i in range(len(bin_str)):
        nm.update({neighbors[i]: bin_str[i]})
    for key, value in funct.items():
        for cord_list in value:
            sum = 0
            for cord in cord_list:
                sum += int(nm[cord])
            if sum != key:
                return False
    return True


if __name__ == '__main__':
    gridsize = 6
    n_mines = 3
    sweeper = Mines(gridsize, n_mines)
    sweeper.showcurrent()
    grid = sweeper.checkcell((0, 0))
    functions = {}
    empty_neighbors = gen_functions(sweeper, grid, functions)
    print("empty neighbors", empty_neighbors)
    print("functions:", functions)
    print("sweeper", sweeper.flags)
    print(int("111111", 2))
    print(check_if_true("0"*len(empty_neighbors), empty_neighbors, sweeper.flags, functions))
