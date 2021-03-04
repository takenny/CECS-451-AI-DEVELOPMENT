from mines import Mines


# class to container boundary data
class BCell:

    def __init__(self, value, neighbors=[], flags=0):
        self.value = value
        self.flags = flags
        self.neighbors = neighbors


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
                flags = 0
                neighbors.clear()
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < len(grid) and 0 <= j+y < len(grid):
                            if grid[i+x][j+y] == ' ':
                                if (i+x, j+y) not in empty_neighbors and (i+x,j+x) not in sweeper.flags:
                                    empty_neighbors.append((i+x, j+y))
                                if (i+x, j+y) in sweeper.flags:
                                    flags += 1
                                neighbors.append((i+x, j+y))
                # if there is only one neighbor it can be added to the flag list
                if len(neighbors) == int(grid[i][j]):
                    for cord in neighbors:
                        if cord not in sweeper.flags:
                            sweeper.flags.append(cord)
                elif len(neighbors) > 0:
                    functions.update({(i, j): BCell(grid[i][j], neighbors, flags)})
    print("flags: ", len(sweeper.flags), sweeper.flags)
    print("neighbors: ", len(empty_neighbors), empty_neighbors)

    for cell in empty_neighbors:
        empty_neighbors.remove(cell)

    return empty_neighbors


def remove_cell(functions, empty_neighbors, cell):
    if cell in empty_neighbors:
        empty_neighbors.remove(cell)
    for key, value in functions.copy().items():
        if cell in value.neighbors:
            value.neighbors.remove(cell)
        print(key, "flags:", value.flags, "value:", value.value, value.neighbors)
        if value.flags == int(value.value):
            for cord in value.neighbors:
                print(key, "flags:", value.flags, "value:", value.value, value.neighbors)
                sweeper.checkcell(cord)
                sweeper.showcurrent()
            functions.pop(key)



def enumerate_combos(empty_neighbors, sweeper, functions):
    # append to list if true
    safe_mine = [[], []]
    listOfStrings = []
    diff = 0

    for i in range(int('1'*len(empty_neighbors), 2)+1):
        binstring = "0" + str(len(empty_neighbors)) + "b"
        binary = format(i, binstring)
        if check_if_true(binary, empty_neighbors, sweeper.flags, functions):
            listOfStrings.append(binary)
    transposed_list = list(map(list, zip(*listOfStrings)))
    for i in range(len(transposed_list)):
        if '1' not in transposed_list[i] and empty_neighbors[i] not in safe_mine[0]:
            safe_mine[0].append(empty_neighbors[i])
        if '0' not in transposed_list[i] and empty_neighbors[i] not in safe_mine[1]:
            safe_mine[1].append(empty_neighbors[i])

    return safe_mine


def check_if_true(bin_str, neighbors, flags, funct):
    nm = {}
    # print(functions)
    for i in range(len(bin_str)):
        nm.update({neighbors[i]: bin_str[i]})
    for key, value in funct.items():
        sum = value.flags
        for cord in value.neighbors:
            sum += int(nm[cord])
        if sum != int(value.value):
            return False
    return True


if __name__ == '__main__':
    gridsize = 16
    n_mines = 40
    sweeper = Mines(gridsize, n_mines)
    sweeper.showcurrent()
    functions = {}

    while not sweeper.isfail() and not sweeper.checkmines():
        print(sweeper.isfail(), sweeper.checkmines())
        print("starting gen functions")
        empty_neighbors = gen_functions(sweeper, functions)
        # print(empty_neighbors)
        print("end gen functions")
        print("start enumerate")
        safe = enumerate_combos(empty_neighbors, sweeper, functions)
        print("end enumerate")

        for cell in safe[0]:
            sweeper.checkcell(cell)
            sweeper.showcurrent()
        for mine in safe[1]:
            if mine not in sweeper.flags:
                sweeper.flags.append(mine)
        print("safe:", len(safe[0]), "flags:", len(sweeper.flags))
