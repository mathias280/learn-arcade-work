# Lab 8
import arcade
import random

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_FOOD = 0.40
SPRITE_SCALING_VILLAIN = 0.40

FOOD_COUNT = 80
VILLAIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "Lab 8 - Sprites"


class Villain(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super(). __init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x = -2

        if self.right > SCREEN_WIDTH:
            self.change_x = -2

        if self.bottom < 0:
            self.change_y = -2

        if self.top > SCREEN_HEIGHT:
            self.change_y = -2

# 2nd option
    # def reset_pos(self):
        # self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        # self.center_x = random.randrange(SCREEN_WIDTH)

    # def update(self):
        # self.center_y += 3
        # if self.top < -0:
            # self.reset_pos()


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
        self.villain_sprite_list = None
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
        self.villain_sprite_list = arcade.SpriteList()

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

        for i in range(VILLAIN_COUNT):
            # Create Villain (kenny.nL)
            villain = Villain("Villain.png", SPRITE_SCALING_VILLAIN)

            villain.center_x = random.randrange(SCREEN_WIDTH)
            villain.center_y = random.randrange(SCREEN_HEIGHT)
            villain.change_x = random.randrange(-3, 4)
            villain.change_y = random.randrange(-3, 4)

            self.villain_sprite_list.append(villain)

    def on_draw(self):

        arcade.start_render()
        self.food_sprite_list.draw()
        self.player_sprite_list.draw()
        self.villain_sprite_list.draw()

        # Text
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        # Character movement
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):

        self.food_sprite_list.update()
        self.villain_sprite_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.food_sprite_list)
        for food in hit_list:
            food.remove_from_sprite_lists()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.villain_sprite_list)
        for villain in hit_list:
            villain.remove_from_sprite_lists()
            self.score -= 1


def main():
    window = SpritesGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
