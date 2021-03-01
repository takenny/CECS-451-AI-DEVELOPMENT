from mines import Mines


def gen_functions(sweeper, grid, functions):
    functions.clear()

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != '0' and grid[i][j] != ' ':
                if grid[i][j] not in functions:
                    functions.update({grid[i][j]: []})

                # Check neighbors in all directions to see if they are empty
                neighbors = []
                neighbors.clear()
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < len(grid) and 0 <= j+y < len(grid):
                            if grid[i+x][j+y] == ' ':
                                neighbors.append((i+x, j+y))
                if len(neighbors) == 1 and neighbors[0] not in sweeper.flags:
                    sweeper.flags.append(neighbors[0])
                elif len(neighbors) > 1:
                    functions[grid[i][j]].append(neighbors)


if __name__ == '__main__':
    gridsize = 6
    n_mines = 3
    sweeper = Mines(gridsize, n_mines)
    sweeper.showcurrent()
    grid = sweeper.checkcell((0, 0))
    functions = {}
    gen_functions(sweeper, grid, functions)
    print(functions)
    print(sweeper.flags)
