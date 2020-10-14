# Lab 8
import arcade
import random
import os

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_FOOD = .35
FOOD_COUNT = 80

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 8 - Sprites"


class Food(arcade.Sprite):

    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class SpritesGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # VARIABLES
        self.player_sprite_list = None
        self.food_sprite_list = None

        # Player
        self.player_sprite = None
        self.score = 0

        # Cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):

        self.player_sprite_list = arcade.SpriteList()
        self.food_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Character (Kenny.nL)
        self.player_sprite = arcade.Sprite("Xavier.png", SPRITE_SCALING_PLAYER)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        # Food
        for i in range(FOOD_COUNT):

            # Create Food
            food = Food("Food.png", SPRITE_SCALING_FOOD)

            food.center_x = random.randrange(SCREEN_WIDTH)
            food.center_y = random.randrange(SCREEN_HEIGHT)

            self.food_sprite_list.append(food)

    def on_draw(self):

        arcade.start_render()
        self.food_sprite_list.draw()
        self.player_sprite_list.draw()

        # Text
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        # Character movement
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):

        self.food_sprite_list.update()

        food_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.food_sprite_list)

        # Loop
        for food in food_hit_list:
            food.remove_from_sprite_lists()
            self.score += 1


def main():
    window = SpritesGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
