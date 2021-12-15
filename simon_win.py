"""
Simon says. Try to replay a sequence.
"""

import sys, random
import pygame
from pygame.locals import *
from state import *
from grid import *

class SimonSays:
    """
    Main game logic
    """
    def __init__(self, width, height):
        # Initialize pygame
        self.screen = pygame.display.set_mode((width, height))
        pygame.init()
        pygame.font.init()

        # Build the grid used to display the game
        self.grid = Grid(width, height)
        self.grid.add_square(Square(pygame.Color(200, 0, 0)))
        self.grid.add_square(Square(pygame.Color(0, 200, 0)))
        self.grid.add_square(Square(pygame.Color(0, 0, 200)))
        self.grid.add_square(Square(pygame.Color(200, 200, 0)))

        # Create the default font used when drawing overlays
        self.font = pygame.font.Font(None, 200)
        self.font.set_bold(True)

        # Create the FSM used to maintain and transition game state
        self.fsm = Fsm()

    def restart(self):
        self.sequence = []
        self.position = 0
        self.fsm.transition(self, 'start')

    def next_level(self):
        """
        Tell the FSM to go to the next level
        """
        self.position = 0
        self.draw()
        self.fsm.transition(self)

    def add_sequence(self):
        """
        Add a computer input value to the sequence and return the new sequence
        """
        pressed = random.randint(1, 4)
        self.sequence.append(pressed)
        return self.sequence

    def press(self, number):
        """
        Respond to a user guess
        """
        self.grid.clear()
        self.grid.squares[number - 1].pressed = True
        self.draw()
        self.position = self.position + 1
        if self.sequence[self.position - 1] != number:
            # The guess was incorrect!
            raise RuntimeError('Invalid choice')

    def draw(self, text=None):
        """
        Draws the game Grid with an optional text overlay
        """
        self.screen.fill((255, 255, 255))
        current = 0
        for s in self.grid.squares:
            current = current + 1
            if s.pressed == False:
                pygame.draw.rect(self.screen, s.color, s.rect)
                render = self.font.render(str(current), 0, (0, 0, 0))
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), s.rect)
                render = self.font.render(str(current), 0, (255, 255, 255))
            self.screen.blit(render, (s.rect.centerx - 50, s.rect.centery - 50))

        if text:
            self.render_overlay(text)
        pygame.display.flip()

    def render_overlay(self, text):
        """
        Draws a text overlay and translucent background over the board
        """
        s = pygame.Surface((1024, 768))
        s.set_alpha(200)
        s.fill((255, 255, 255))
        self.screen.blit(s, (0, 0))
        render = self.font.render(text, 0, (0, 0, 0))
        self.screen.blit(
            render,
            (self.screen.get_rect().centerx - render.get_rect().centerx,
             self.screen.get_rect().centery - render.get_rect().centery)
        )

def main():
    SimonSays(1024, 768).restart()

if __name__ == '__main__':
    sys.exit(main())