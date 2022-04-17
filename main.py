import sys
import pygame
from autosolver import AutoSolver


def read_grid(filename) -> list[list[int]]:
    """
    Reads the contents in `filename` and returns the represented grid
    :param filename:
    :return: The list representation of a Sudoku grid
    :rtype: list[list[int]]
    """
    grid = []
    with open(filename, "r") as f:
        for line in f.readlines():
            grid.append(line.strip("\n").split(","))

    return [[int(grid[i][j]) for j in range(len(grid))] for i in range(len(grid))]


def file_exists(filename: str) -> bool:
    """
    Checks that the specified file exists
    :param filename: The name of the file to check
    :return: If the file exists or not
    :rtype: bool
    """
    try:
        f = open(filename, "r")
        f.close()
    except FileNotFoundError:
        print(f"\u001b[31m[FileNotFoundError]: The file '{filename}' was not found.\u001b[0m")
        return False

    return True


def main(filename: str):
    """
    Reads the grid from the file and then runs the auto-solver
    :param filename: Filename of the Sudoku grid
    """
    grid = read_grid(filename)
    AutoSolver(grid)


if __name__ == "__main__":
    # Checking for a filename
    if len(sys.argv) != 2:
        print(f"\u001b[31m[Error]: Needs to be followed by a filename.\u001b[0m")
        filename = input("Enter puzzle filename: ")
    else:
        filename = sys.argv[1]
    # Checking the file exists
    if not file_exists(filename):
        exit()

    # Runs the solver
    main(filename)

    # Keeps the window open until the user shuts it
    keep_open = True
    while keep_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_open = False

    pygame.display.quit()
