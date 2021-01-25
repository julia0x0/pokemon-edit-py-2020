import pygame, sys, os
from shape import Rectangle, Container, Text, Color
# from modes import *


class Program(Container):
    def __init__(self, screen_size: tuple = (720, 480), path: str = os.path.join("..", "saves", "untitled"), caption: str = "Create a Pokemon Game"):
        self.size = screen_size
        self.path = path
        self.caption = caption
        pygame.init()
        self.shape_pos = None
        self.buttons = []
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)
        super().__init__(screen_size)
        button_names = ["DRAW", "EDIT", "ATTR"]
        increase = 480/screen_size[1]
        self.font_size = int(30*increase)
        self.font = pygame.font.SysFont("Arial", self.font_size)
        space = 5*increase
        size = (15*increase, 40*increase)
        for i, y in enumerate(range(int(space), int(space*(len(button_names)+1)), int(space))):
            button = Rectangle(size, (space, y), Text(button_names[i-1], self.font), Color(0, 0, 0))
            self.buttons.append(button)
        self.screen.blit(self, self.position)
        err_code = self.main()
        self.stop(err_code)

    def main(self):
        while True:
            for event in [pygame.event.wait()]+pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("DOWN")
                    self.shape_pos = event.pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    print("UP")
                    x, y = event.pos
                    if self.shape_pos:
                        shape = Rectangle((abs(x-self.shape_pos[0]), abs(y-self.shape_pos[1])), self.shape_pos)
                        self.shapes.append(shape)
                        self.shape_pos = None
            self.update()

    def update(self):
        pygame.display.update()
        super().update()
        for button in self.buttons:
            self.draw(button)

    def save(self):
        pass

    def stop(self, err_code: int):
        print(err_code)
        self.save()
        pygame.exit()
        sys.exit()
