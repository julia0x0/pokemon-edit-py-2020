import pygame, os
from shape import *
# from modes import *


class Program(Container):
    def __init__(self, screen_size: tuple = (1920, 1080), path: str = os.path.join("..", "saves", "untitled"), caption: str = "Create a Pokemon Game"):
        self.path = path
        self.caption = caption
        self.shape = None
        self.buttons = []
        button_names = ["DRAW", "EDIT", "ATTR"]
        increase = 480/screen_size[1]
        space = 5*increase
        size = (15*increase, 40*increase)
        for i, y in enumerate(range(int(space), int(space*(len(button_names)+1)), int(space))):
            button = Rectangle(size, (space, y), Text(button_names[i]), Color(0, 0, 0))
            self.buttons.append(button)
        super().__init__(screen_size)

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self.caption)
        self.screen.blit(self, self.position)
        err_code = self.main()
        self.stop(err_code)

    def main(self):
        while True:
            for event in [pygame.event.wait()]+pygame.event.get():
                if event == pygame.QUIT:
                    return 0
                if event == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.check_mouse_down(x, y)
            self.update()

    def check_mouse_down(self, x: int, y: int):
        if self.shape:
            self.shape.resize(x, y)
        else:
            self.shape = Rectangle((0, 0), (x, y))

    def update(self):
        super().update()
        if self.shape:
            self.draw(self.shape)
        for button in self.buttons:
            self.draw(button)
        pygame.display.update()

    def save(self):
        pass

    def stop(self, err_code: int):
        print(err_code)
        self.save()
        pygame.exit()
        sys.exit()
