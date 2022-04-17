from __future__ import annotations
import pygame
import time
from gui import WIDTH, HEIGHT, SolverGUI


class AutoSolver:
    """
    Automatically solves a Sudoku grid and animates it for the user.
    """
    def __init__(self, grid: list[list[int]]):
        """
        :param grid: The list representation of the Sudoku grid.
        """
        self.window = None
        presets = [[grid[i][j] != 0 for j in range(9)] for i in range(9)]
        self.start_time = time.time()
        self.gui = None
        self.__start(grid, presets)

    def __start(self, grid_list: list[list[int]], presets: list[list[bool]]) -> None:
        """
        Starts the solving process and creates the window for the display
        :param grid_list: The list representation of the Sudoku grid
        :param presets: The representation of the grid where all initial value locations are True and everything else is False
        """
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku Auto-Solver: Time Taken: 00:00")
        self.gui = SolverGUI(self.window, presets, self.start_time)
        self.__step(grid_list, presets)
        print("Done")

    def __step(self, grid: list[list[int]], presets: list[list[bool]]) -> bool:
        """
        Completes one step of the solving process
        :param grid: The list representation of the Sudoku grid
        :param presets: The representation of the grid where all initial value locations are True and everything else is False
        :return: If the step was successful (is the grid still valid).
        :rtype: bool
        """
        if self.__check_events_exit():
            exit()

        # Finding the next empty square in the grid
        next_empty = self.find_empty(grid)
        if next_empty == (-1, -1):
            return True
        row, col = next_empty
        # Goes through each possible number and attempts to put it in the square.
        for i in range(1, 10):
            # Check to see if is valid choice.
            if self.valid(grid, i, (row, col)):
                grid[row][col] = i
                self.gui.redraw(grid, next_empty)
                if self.__step(grid, presets):
                    return True

                # If step fails then the square is reset.
                grid[row][col] = 0
                # AutoSolverGUI.redraw(self.window, grid, next_empty, presets, self.start_time)
                self.gui.redraw(grid, next_empty)
        return False

    @staticmethod
    def __check_events_exit() -> bool:
        """
        Checks to see if a `pygame` `QUIT` event has triggered.
        :return: If there is a `pygame.QUIT` event
        :rtype: bool
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    @staticmethod
    def find_empty(grid: list[list[int]]) -> tuple[int, int]:
        """
        Finds the first empty square in the grid and returns its location
        :param grid: The list representation of the Sudoku grid
        :return: The location of the next empty square or (-1, -1) if there are no empty squares.
        :rtype: tuple[int, int]
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return i, j
        return -1, -1

    @staticmethod
    def copy_grid(grid: list[list[int]]):
        """
        Creates a copy of the grid
        :param grid: The grid to be copied
        :return: The copy of the passed grid
        :rtype: list[list[int]]
        """
        return [[grid[i][j] for j in range(9)] for i in range(9)]

    @staticmethod
    def valid(grid: list[list[int]], num: int, pos: tuple[int, int]) -> bool:
        """
        Checks if the insertion of `num` at `pos` is valid
        :param grid: The representation of the Sudoku grid
        :param num: The number being put in the square
        :param pos: The position of the number being added
        :return: If the move is valid or not.
        :rtype: bool
        """
        # Checking the rows/columns
        for i in range(len(grid[0])):
            if grid[pos[0]][i] == num and pos[1] != i:
                return False
        for i in range(len(grid)):
            if grid[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        # Checking the box
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if grid[i][j] == num and (i, j) != pos:
                    return False
        return True




