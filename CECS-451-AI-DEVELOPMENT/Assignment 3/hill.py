from board import Board
import copy
import time
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
START_TIME = time.time()


def hill():
    # create a random initial state and its fitness
    current_state = Board(NUM_QUEENS)
    current_state.fitness()
    random_restart = 0

    # used to check if a solution is found
    # solution not found, but there are no successors with a better fitness
    local_min = False
    # solution found
    global_min = False

    # loop until solution found
    while not global_min:
        # go though each row in the board
        for i in range(NUM_QUEENS):
            # if the current state is the solution, we can stop
            if current_state.get_fit() == 0:
                global_min = True
                break

            # if current state is a local min, then generate a new board
            if local_min:
                current_state = Board(NUM_QUEENS)
                current_state.fitness()
                random_restart += 1

            # make a copy of the current state
            next_state = copy.deepcopy(current_state)

            # make the row all zeros
            next_state.get_map()[i] = [0]*NUM_QUEENS
            # if no successor is chosen this will remain true
            local_min = True

            # put the queen in different positions in the board and check fitness
            for j in range(NUM_QUEENS):
                next_state.flip(i, j)
                next_state.fitness()

                # if successor fitness is lower than current state fitness, make that the new current state
                if next_state.get_fit() < current_state.get_fit():
                    current_state = copy.deepcopy(next_state)
                    local_min = False
                next_state.flip(i, j)

    # Print solution
    run_time = round((time.time() - START_TIME)*1000, 2)
    print("Run time: %2.2fms" % run_time)
    print("# of random restart:", random_restart)
    current_state.show()


hill()
