import os

import pygame

from .maze import Maze
class Game:
    def __init__(self):
        self._running = True
        self._screen = None
        self.size = self.width, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        print("on event")
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init():
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


class App:
    def run(self):
        print(os.path.dirname(__file__))

        file_path = os.path.join(os.path.dirname(
            __file__), "assets", "level.txt")
        print(file_path)

        Maze.read_maze(file_path)

        print(Maze.random_empty_tile())
        Maze.print()

        game = Game()
        game.on_execute()
