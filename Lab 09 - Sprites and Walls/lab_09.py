import arcade
import random
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE =

VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 6


class BoxGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title):

        # Sprite lists
        self.player_list = None

        # Player Set up
        self.player_list = None

        self.coin_list = None
        self.wall_list = None

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        self.player_list = arcade


