#small function for the dead state, basically turning every cell in the grid to 0 wich is used as initialization for the "new_state" in the "next_board_state" function
def dead_state(w, h):
    return [[0 for _ in range(w)] for _ in range(h)]



