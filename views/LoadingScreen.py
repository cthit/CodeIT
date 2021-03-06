import os

import pygame

from src.GameMethods import GameMethods
from src.gui.elements.image.Image import Image
from src.gui.elements.text.TextBlock import TextBlock


def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(TextBlock("Loading next level", 200, 200))
    path = os.path.dirname(os.path.realpath(__file__)) + "/../resources/funtique/FuntiqueGUI_0001_Loader.png"
    loading_image = pygame.image.load(path)
    loading_image = pygame.transform.scale(loading_image, (40, 40))
    gui.add_gui_element(Image(300, 300, 1, 1, loading_image))
