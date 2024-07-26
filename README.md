# The-Game-of-Life

## Overview

This project is a variation of Conway's Game of Life with two competing cell types: red and blue. It runs on a toroidal grid, meaning the edges wrap around.

## Features

Toroidal Grid: Edges wrap around to the opposite side.

Competing Cells: Red and blue cells evolve and compete.

Custom Initialization: Set probabilities for each cell type.

Colorful Output: Visualize the grid in the terminal with colors.

## How It Works

random_state(w, h): Initializes the grid with random values.

render(board_state): Displays the grid in the terminal.

get_alive_neighbors(state, x, y): Counts neighbors for each cell type.

next_board_state(current_state): Computes the next state based on rules.

## License

This project is licensed under the MIT License.
