import random
import settings
import utils
import os
import time

def random_state(w, h):

    state = utils.dead_state(w, h)
    #weight initialization
    weights = [8, 1, 1] #blank, red, blue 
    
    for i in range(h):
        for j in range(w):
            state[i][j] = random.choices([0, 1, 2], weights=weights, k=1)[0] 

    return state


def render(board_state):
    os.system('cls' if os.name == 'nt' else 'clear')  
    for row in board_state:
        line = "|"
        for cell in row:
            if cell == 1:
                line += "\033[31m#\033[0m "  #Red 
            elif cell == 2:
                line += "\033[34m#\033[0m "  #Blue 
            else:
                line += "  "  
        line += "|"
        print(line)


def get_alive_neighbors(state, x, y):
    h = len(state)
    w = len(state[0])
    neighbors = [0, 0, 0]

    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    for dx, dy in directions:
        nx = (x + dx) % h
        ny = (y + dy) % w
        neighbors[state[nx][ny]] += 1

    return neighbors


def next_board_state(current_state):
    h = len(current_state)
    w = len(current_state[0])
    new_state = utils.dead_state(w, h)

    for x in range(h):
        for y in range(w):
            neighbors = get_alive_neighbors(current_state, x, y)
            total_neighbors = neighbors[1] + neighbors[2]

            if current_state[x][y] == 1:
                if total_neighbors < 2 or total_neighbors > 3:
                    new_state[x][y] = 0
                else:
                    new_state[x][y] = 1

            elif current_state[x][y] == 2:
                if total_neighbors < 2 or total_neighbors > 3:
                    new_state[x][y] = 0
                else:
                    new_state[x][y] = 2
            
            else:
                if total_neighbors == 3:
                    if neighbors[1] > neighbors[2]:
                        new_state[x][y] = 1
                    else:
                        new_state[x][y] = 2

    return new_state

    

#test
os.system('cls' if os.name == 'nt' else 'clear')  
state = random_state(settings.b_width, settings.b_height)

while True:
    render(state)
    state = next_board_state(state)
    time.sleep(0.2) 
