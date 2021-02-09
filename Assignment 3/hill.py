from board import Board
import copy
'''
############## Hill Climbing ###############
1. Initialize at random state.

2. Generate successors and check the fitness of each one
    - The one with the lowest random state (less than the current state)
        is the new current state

    For each row try placing the queen in different positions and check the fitness
        - The board with the lowest fitness becomes the new board (state)

3. If fitness of current state is 0, then the solution is reached and ca••••n
    end loop
    - If none of the successors are less than the current state, then create
        new random state

hill-climbing:
    create new random board

    while fitness is not 0 or local_min not reached:
        for each row in the board:
            if current state has fitness of 0:
                solution found
            else move the queen to all the possible positions and check the fitness
                if non of the other combinations have a lower fitness:
                    local min reached
                    generate new random board and restart process
                else:
                    state with lowest fitness is new current state
'''
NUM_QUEENS = 5


def hill():
    current_state = Board(NUM_QUEENS)
    current_state.fitness()
    # current_state.show()
    local_min = False
    global_min = False

    while not global_min and not local_min:
        for i in range(NUM_QUEENS):
            if current_state.get_fit() == 0:
                global_min = True
            if global_min or local_min:
                break
            next_state = copy.deepcopy(current_state)
            next_state.get_map()[i] = [0]*NUM_QUEENS
            local_min = True
            for j in range(NUM_QUEENS):
                next_state.flip(i, j)
                next_state.fitness()
                if next_state.get_fit() < current_state.get_fit():
                    current_state = copy.deepcopy(next_state)
    if local_min:
        hill()
    elif global_min:
        current_state.show()


hill()
