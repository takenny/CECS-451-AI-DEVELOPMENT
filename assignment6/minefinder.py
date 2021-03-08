from mines import Mines


# class to container boundary data
class BCell:

    def __init__(self, value, neighbors=[], flags=0):
        self.value = value
        self.flags = flags
        self.neighbors = neighbors
        self.prob = int(self.value)/len(self.neighbors)


def gen_functions():
    functions.clear()
    empty_neighbors = []
    empty_neighbors.clear()
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
                        ix = i + x
                        jy = j + y
                        if 0 <= ix < len(grid) and 0 <= jy < len(grid):
                            if grid[ix][jy] == ' ':
                                if (ix, jy) not in sweeper.flags:
                                    if (ix, jy) not in empty_neighbors:
                                        empty_neighbors.append((ix, jy))
                                else:
                                    flags += 1
                                neighbors.append((ix, jy))

                # if there is only one neighbor it can be added to the flag list
                if len(neighbors) == int(grid[i][j]):
                    for cord in neighbors:
                        if cord not in sweeper.flags:
                            sweeper.flags.append(cord)
                elif len(neighbors) > 0:
                    functions.update({(i, j): BCell(grid[i][j], neighbors, flags)})

    return empty_neighbors


def optimize_functions():

    for cell in empty_neighbors.copy():
        if cell in sweeper.flags:
            empty_neighbors.remove(cell)

    for key, value in functions.copy().items():
        # print(key, [key for key, value in functions])
        for cell in value.neighbors.copy():
            if cell in sweeper.flags:
                value.neighbors.remove(cell)


def remove_safe_from_functions():
    for cell, data in functions.items():
        # print("cell:", cell, "value:", data.value, "flags:", data.flags, "neighbors:", data.neighbors)
        if int(data.value) == data.flags:
            temp = [c for c in data.neighbors]
            if data.neighbors[0] not in sweeper.flags:
                print("removed using function", data.neighbors[0])
                sweeper.checkcell(data.neighbors[0])
                sweeper.showcurrent()
                return True
    return False


def separate_neighbors():
    temp = []
    first = True
    for cell, data in functions.items():
        if first:
            temp.append(data.neighbors)
            first = False
        else:
            part_of_group = False
            for i in range(len(temp)):
                if any(item in data.neighbors for item in temp[i]):
                    for item in data.neighbors:
                        if item not in temp[i]:
                            temp[i].append(item)
                    part_of_group = True
            if not part_of_group:
                temp.append(data.neighbors)
    return temp


def enumerate_combos():
    # append to list if true
    safe_mine = [[], []]
    listOfStrings = []
    diff = 0

    for group in empty_neighbors:
        group_size = len(group)
        for i in range(int('1'*group_size, 2)+1):
            binstring = "0" + str(group_size) + "b"
            binary = format(i, binstring)
            if check_if_true(binary, group):
                listOfStrings.append(binary)
    transposed_list = list(map(list, zip(*listOfStrings)))
    for i in range(len(transposed_list)):
        if '1' not in transposed_list[i] and group[i] not in safe_mine[0]:
            safe_mine[0].append(group[i])
        if '0' not in transposed_list[i] and group[i] not in safe_mine[1]:
            safe_mine[1].append(grou[i])

    return safe_mine


def check_if_true(bin_str, group):
    nm = {}
    for i in range(len(bin_str)):
        nm.update({group[i]: bin_str[i]})
    for key, value in functions.items():
        sum = value.flags
        for cord in value.neighbors:
            if cord in nm:
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
        print("start annoying print")
        i_hate_this_project = True  # This is true
        while i_hate_this_project:
            empty_neighbors = gen_functions()
            optimize_functions()
            i_hate_this_project = remove_safe_from_functions()
        print("end annoying print")
        if sweeper.checkmines():
            break
        else:
            empty_neighbors = separate_neighbors()
            print("start enumerate")
            safe = enumerate_combos()
            print("end enumerate")

            for cell in safe[0]:
                sweeper.checkcell(cell)
                sweeper.showcurrent()

            for mine in safe[1]:
                if mine not in sweeper.flags:
                    sweeper.flags.append(mine)


if sweeper.checkmines():
    print("It's Solved!")
