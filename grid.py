import pygame

class Grid:
    """
    Grid class that holds Square objects
    """
    def __init__(self, width, height):
        self.square_width = width / 2
        self.square_height = height / 2
        self.squares = []
        self.square_positions = {
            1: (0, 0),
            2: (self.square_width, 0),
            3: (0, self.square_height),
            4: (self.square_width, self.square_height)
        }

    def add_square(self, square):
        self.squares.append(square)
        square.number = len(self.squares)
        square.rect = pygame.Rect(
            self.square_positions.get(len(self.squares)),
            (self.square_width, self.square_height)
        )

    def clear(self):
        for s in self.squares:
            s.pressed = False

class Square:
    """
    Input targets that determine sequences
    """
    def __init__(self, color):
        self.color = color
        self.rect = None
        self.pressed = False
        self.number = None