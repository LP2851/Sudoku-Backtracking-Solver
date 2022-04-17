import pygame
import time
pygame.font.init()

# Window width and height
WIDTH, HEIGHT = 540, 540
# Wait between each update
FRAME_SLEEP = 0.1


class SolverGUI:
    """
    Handles the drawing of the GUI
    """
    def __init__(self, window, presets: list[list[bool]], start_time: float):
        """
        :param window: The window object being used
        :param grid: The current representation of the Sudoku grid
        :param presets: The representation of the grid where all initial value locations are True and everything else is False
        :param start_time: The start time of the solver
        """
        self.__window = window
        self.__presets = presets
        self.__start_time = start_time

    def redraw(self, grid: list[list[int]], focus: tuple[int, int]) -> None:
        """
        Redraws the window with the new grid and new focus
        :param grid: The next representation of the Sudoku grid
        :param focus: The current square the solver is working on
        """
        play_time = round(time.time() - self.__start_time)
        pygame.display.set_caption(f"Sudoku Auto-Solver: Time Taken: {self.format_time(play_time)}")
        # white
        self.__window.fill((255, 255, 255))

        # Draws grid
        self.__draw_grid()

        # Draws the squares
        for i in range(9):
            for j in range(9):
                self.__draw_square(grid[i][j], i, j, ((i, j) == focus))

        pygame.display.update()
        time.sleep(FRAME_SLEEP)

    def __draw_grid(self) -> None:
        """
        Draws the gridlines
        """
        line_gap = WIDTH / 9
        for i in range(10):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.__window, (0, 0, 0), (0, i * line_gap), (WIDTH, i * line_gap), thickness)
            pygame.draw.line(self.__window, (0, 0, 0), (i * line_gap, 0), (i * line_gap, HEIGHT), thickness)

    def __draw_square(self, value: int, row: int, col: int, focused: bool) -> None:
        """
        Draws an individual square (number and focus box if necessary)
        :param value: The value in the grid position
        :param row: The row of the value
        :param col: The column of the value
        :param focused: If the square is focused or not
        """
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = WIDTH / 9
        x = col * gap
        y = row * gap

        if not (value == 0):
            # Showing presets as black; inputted as red
            color = (0, 0, 0) if self.__presets[row][col] else (255, 0, 0)
            text = fnt.render(str(value), True, color)
            self.__window.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if focused:
            pygame.draw.rect(self.__window, (255, 0, 0), (x, y, gap, gap), 3)

    @staticmethod
    def format_time(secs: float) -> str:
        """
        Formats the timer to be in the form mm:ss
        :param secs: The number of seconds since the start
        :return: The formatted timer as a string
        :rtype: str
        """
        sec = secs % 60
        minute = secs // 60

        sec = str(sec) if sec >= 10 else "0" + str(sec)
        minute = str(minute) if minute >= 10 else "0" + str(minute)
        return f"{minute}:{sec}"


# Rewritten for class above
#
# class AutoSolverGUI:
#     """
#     Handles the drawing of the GUI
#     """
#     @staticmethod
#     def redraw(window, grid: list[list[int]], focus: tuple[int, int], presets: list[list[bool]], start_time: float):
#         play_time = round(time.time() - start_time)
#         pygame.display.set_caption(f"Sudoku Auto-Solver: Time Taken: {AutoSolverGUI.format_time(play_time)}")
#         # white
#         window.fill((255, 255, 255))
#         # Draw grid and board
#         AutoSolverGUI.__draw_grid(window, grid, focus, presets)
#         pygame.display.update()
#         time.sleep(FRAME_SLEEP)
#
#     @staticmethod
#     def __draw_grid(window, grid: list[list[int]], focus: tuple[int, int], presets: list[list[bool]]) -> None:
#         line_gap = WIDTH / 9
#         for i in range(10):
#             if i % 3 == 0 and i != 0:
#                 thickness = 4
#             else:
#                 thickness = 1
#             pygame.draw.line(window, (0, 0, 0), (0, i * line_gap), (WIDTH, i * line_gap), thickness)
#             pygame.draw.line(window, (0, 0, 0), (i * line_gap, 0), (i * line_gap, HEIGHT), thickness)
#
#         for i in range(9):
#             for j in range(9):
#                 AutoSolverGUI.__draw_square(window, grid[i][j], i, j, ((i, j) == focus), presets)
#
#     @staticmethod
#     def __draw_square(window, value, row: int, col: int, focused: bool, presets: list[list[bool]]) -> None:
#         fnt = pygame.font.SysFont("comicsans", 40)
#
#         gap = WIDTH / 9
#         x = col * gap
#         y = row * gap
#
#         if not (value == 0):
#             # showing presets as black, inputted as red
#             color = (0, 0, 0) if presets[row][col] else (255, 0, 0)
#             text = fnt.render(str(value), True, color)
#             window.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
#
#         if focused:
#             pygame.draw.rect(window, (255, 0, 0), (x, y, gap, gap), 3)
#
#     @staticmethod
#     def format_time(secs: float) -> str:
#         sec = secs % 60
#         minute = secs // 60
#
#         sec = str(sec) if sec >= 10 else "0" + str(sec)
#         minute = str(minute) if minute >= 10 else "0" + str(minute)
#         return f"{minute}:{sec}"
