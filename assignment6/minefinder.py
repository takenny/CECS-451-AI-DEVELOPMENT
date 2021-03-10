from mines import Mines
import copy
import time

start_time = time.time()

# class to container boundary data
class BCell:
    # Value (str): is the value of the cell. This is a string
    # Flags (int): is the number of flags that neighbor the cell.
    # neighbors: is a list of coodinates for all the empy neighbors
    # prob (float): is the local probability that there is a mine for each of the empty cells
    def __init__(self, value, neighbors=[], flags=0):
        self.value = value
        self.flags = flags
        self.neighbors = neighbors
        self.prob = (int(self.value)-self.flags)/len(self.neighbors)


# Generate the functions
def gen_functions():
    # Clear functions from previous game loop
    functions.clear()
    # This is to store the empty neighbors surrounding the boundary
    empty_neighbors = []
    empty_neighbors.clear()
    # Get the game grid
    grid = sweeper.checkcell((0, 0))

    # iterate through each row in the grid
    for i in range(len(grid)):
        for j in range(len(grid)):

            # Check to find the boundary cells
            if grid[i][j] != '0' and grid[i][j] != ' ':

                # Check neighbors in all directions to see if they are empty
                neighbors = []  # Neighbors for the current cell
                flags = 0  # The number of flags neighboring the current cell
                neighbors.clear()  # Clear the neighbors from the previous cell

                # Iterate through all the neighbors
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        ix = i + x  # This is the x value of the neighbor
                        jy = j + y  # This is the y value of the neighbor

                        # Make sure we dont go out of bounds of the grid
                        if 0 <= ix < len(grid) and 0 <= jy < len(grid):
                            # check if the neighbor is empty
                            if grid[ix][jy] == ' ':
                                # check that the neighbor is not in flags
                                # and in empty neighbors
                                if (ix, jy) not in sweeper.flags:
                                    if (ix, jy) not in empty_neighbors:
                                        empty_neighbors.append((ix, jy))
                                else:  # if it is in flags increment flags
                                    flags += 1
                                # add to the list of neighbors for the current cell
                                neighbors.append((ix, jy))

                # if the number of neighbors is the same as the value then
                # these are flags
                if len(neighbors) == int(grid[i][j]):
                    for cord in neighbors:
                        if cord not in sweeper.flags:
                            sweeper.flags.append(cord)
                # If it has at least one neighbor add it to functions
                elif len(neighbors) > 0:
                    functions.update({(i, j): BCell(grid[i][j], neighbors, flags)})

    return empty_neighbors


# Removes the flags from neighbors and functions
def optimize_functions():

    # Remove flags from empty neighbors
    for cell in empty_neighbors.copy():
        if cell in sweeper.flags:
            empty_neighbors.remove(cell)

    # Remove flags from all the functions
    for key, value in functions.copy().items():
        # print(key, [key for key, value in functions])
        for cell in value.neighbors.copy():
            if cell in sweeper.flags:
                value.neighbors.remove(cell)


# If the number if flags is the same as the value, then it can be assumed that the rest of the neighbors
# are safe
# For some reason this kept on hitting flags if we tried to check all the cells at once
# so rather than checking all the cells, we run gen functions after each time this runs.
#
# If it checked a cell then it will return true and the main function knows to run gen_functions again
# If it returns false then the main function will not run gen_functions again
def remove_safe_from_functions():
    for cell, data in functions.items():
        if int(data.value) == data.flags:
            if data.neighbors[0] not in sweeper.flags:
                print("removed using function", data.neighbors[0])
                sweeper.checkcell(data.neighbors[0])
                sweeper.showcurrent()
                return True
    return False


# This is to the neighbors into groups
# This reduces the time since it has to calculate 2^n combinations where n is the length of the array.
def separate_neighbors():
    temp = []  # List to hold the empty neighbors data
    first = True  # is this the first time running the loop
    for cell, data in functions.items():
        # If this is the first loop...
        if first:
            temp.append(data.neighbors)  # create sublist
            first = False  # set this to false so that other sublists arent added
        else:
            part_of_group = False  # If this was part of a group this is true
            # iterate through all the neighbor groups
            for i in range(len(temp)):
                # check if any of the neighboring coordinates match any of the coordinates in the group
                if any(item in data.neighbors for item in temp[i]):
                    # Add each of these coordinates to that group if it isnt in it already
                    for item in data.neighbors:
                        if item not in temp[i]:
                            temp[i].append(item)
                    part_of_group = True  # item was part of group
            # if item was not part of any group, create new sublist
            if not part_of_group:
                temp.append(data.neighbors)
    return temp  # Return the seperated groups


# Find the cell with the lowest probability of being a mine
# Currently doesn't work great
# Maybe we should consider non neighboring cells?
def prob_stuck(empty_neighbors):
    probability = {}  # dictionary to hold the probabilities
    # iterate through the empty neighbor groups
    for group in empty_neighbors:
        # iterate though each cell in the group
        for cell in group:
            probability[cell] = 0
            # The number of functions this is part of
            # This is used to get the average
            counter = 0

            # Key: is the key for the map. this is a coordinate (not really used)
            # Value: this is a BCell object
            for key, value in functions.items():
                # check if cell is in the neighbor list
                if cell in value.neighbors:
                    # Add the local probability
                    probability[cell] += value.prob
                    counter += 1
            # Get the average of the probabilities
            probability[cell] /= counter
    # Get the cell with the lowest probability and check that cell
    cell = min(probability, key=probability.get())
    sweeper.checkcell(cell)
    sweeper.showcurrent()


# Create the truth tables in order to find flags and safe cells
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
            safe_mine[1].append(group[i])

    return safe_mine


# Check if the truth string is true
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


# Main
if __name__ == '__main__':
    gridsize = 16
    n_mines = 40
    sweeper = Mines(gridsize, n_mines)
    sweeper.showcurrent()
    functions = {}  # Dictionary to hold the functions
    prev_flags = []  # previous_flags. Used to check if it gets stuck in a loop
    prev_neighbors = []  # List of previous neighbors. also used to check if it get stuck
    safe = []  # safe/flag list

    while not sweeper.isfail() and not sweeper.checkmines():
        safe_values_from_functions = True  # This is true
        # While you can easily get safe values from functions, run continue this loop
        # This helps to keep the length of the neighbor groups down (kinda)
        while safe_values_from_functions:
            empty_neighbors = gen_functions()
            optimize_functions()
            safe_values_from_functions = remove_safe_from_functions()
            prob_stuck(empty_neighbors)
        # If this is already solved, then break out of the loop
        if sweeper.checkmines():
            break
        else:
            # sperate the groups into groups
            empty_neighbors = separate_neighbors()
            # print("start enumerate")
            safe = enumerate_combos()
            # print("end enumerate")

            # Check all the cells in the safe list
            for cell in safe[0]:
                sweeper.checkcell(cell)
                sweeper.showcurrent()

            # Add all the flags to sweeper.flags from the flag list
            for mine in safe[1]:
                if mine not in sweeper.flags:
                    sweeper.flags.append(mine)
            # print("prev_neighbor:", prev_neighbors)
            # print("empty_neighbors: ", empty_neighbors)
            # print("flags:", sweeper.flags)
            # print("loop check: ", (prev_neighbors == empty_neighbors), (prev_flags == sweeper.flags))

            # If the list of neighbors and flags remains the same, we are stuck in a loop and we have to guess a cell
            if prev_neighbors == empty_neighbors and prev_flags == sweeper.flags:
                prob_stuck(empty_neighbors)
                for cell in safe[0]:
                    sweeper.checkcell(cell)
                    sweeper.showcurrent()
            # make copies to check if its stuck in a loop
            prev_flags = copy.deepcopy(sweeper.flags)
            prev_neighbors = copy.deepcopy(empty_neighbors)

if sweeper.checkmines():
    print("It's Solved! in %s seconds" % (time.time() - start_time))
if sweeper.isfail():
    print("It failed in %s seconds" % (time.time() - start_time))

