import sys
import pygame
from pygame.locals import *


class State:
    """
    Handles game state and input
    """
    def enter(self, game):
        pass

    def leave(self, game):
        game.draw()
        pygame.time.wait(1000)

    def wait_for_event(self, type):
        while True:
            pygame.event.set_allowed(type)
            e = pygame.event.wait()
            if e.type == KEYUP and e.key == K_ESCAPE:
                sys.exit()
            pygame.event.set_allowed([KEYUP, KEYDOWN])
            if e.type == KEYUP or e.type == KEYDOWN:
                return e


class StartState(State):
    """
    Prompt the user to begin the game
    """
    def enter(self, game):
        game.draw('Press enter')
        while self.wait_for_event(KEYUP).key != K_RETURN:
            pass
        game.fsm.transition(game)


class LostState(State):
    """
    Let the user know they lost and the level they achieved
    """
    def enter(self, game):
        game.draw('Lost: ' + str(game.position))
        game.grid.clear()
        while self.wait_for_event(KEYUP).key != K_RETURN:
            pass
        pygame.time.wait(1000)
        game.restart()


class PlayerState(State):
    """
    Get input from the player
    """
    def enter(self, game):
        while game.position < len(game.sequence):
            event = self.wait_for_event(KEYDOWN)
            try:
                if event.key == K_1:
                    game.press(1)
                elif event.key == K_2:
                    game.press(2)
                elif event.key == K_3:
                    game.press(3)
                elif event.key == K_4:
                    game.press(4)
            except RuntimeError as error:
                game.fsm.transition(game, 'lost')
            finally:
                self.wait_for_event(KEYUP)
                game.grid.clear()
                game.draw()
        game.next_level()


class ComputerState(State):
    """
    Play the computer's sequence for the user and add a new value
    """
    def enter(self, game):
        # Replay the sequence and pause between each
        for i in game.add_sequence():
            # Show the square as pressed
            game.grid.squares[i - 1].pressed = True
            game.draw()
            pygame.time.wait(400)
            # Show the square as unpressed
            game.grid.squares[i - 1].pressed = False
            game.draw()
            pygame.time.wait(200)

        # Transition back to the player
        game.fsm.transition(game, 'player')


class Fsm:
    """
    Finite state machine
    """
    def __init__(self):
        self.states = {
            'start': StartState(),
            'computer': ComputerState(),
            'player': PlayerState(),
            'lost': LostState()
        }
        self.state = self.states['start']

    def transition(self, game, state=None):
        if (state):
            self.state = self.states[state]
        else:
            self.state.leave(game)
            if isinstance(self.state, StartState):
                self.state = self.states['computer']
            if isinstance(self.state, ComputerState):
                self.state = self.states['player']
            if isinstance(self.state, PlayerState):
                self.state = self.states['computer']
        self.state.enter(game)