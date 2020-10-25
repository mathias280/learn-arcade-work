import random
import arcade

SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_WALL = 0.9
SPRITE_SCALING_FOOD = 0.3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Box Game"

VIEWPORT_MARGIN = 40
Food_AMOUNT = 45
MOVEMENT_SPEED = 6


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player_list = None
        self.player_sprite = None

        self.food_list = None
        self.wall_list = None

        self.physics_engine = None

        self.view_bottom = 0
        self.view_left = 0
        self.score = 0

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("Xavier.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        for x in range(200, 1650, 125):
            for y in range(0, 1250, 50):
                if random.randrange(4) > 0:

                    barrel = arcade.Sprite("Barrel.png", SPRITE_SCALING_WALL)
                    barrel.center_x = x
                    barrel.center_y = y

                    self.wall_list.append(wall)

        for x in range(125, 900, 50):
            wall = arcade.Sprite("Metalwall.png", SPRITE_SCALING_WALL)
            wall.center_x == 200
            wall.center_y == 125

            self.wall_list.append(wall)

        for i in range(Food_AMOUNT):
            food = arcade.Sprite("Food.png", SPRITE_SCALING_FOOD)
            food_placed_successfully = False
            while not food_placed_successfully:
                food.center_x = random.randrange(SCREEN_WIDTH)
                food.center_y = random.randrange(SCREEN_HEIGHT)

                wall_hit_list = arcade.check_for_collision_with_list(food, self.wall_list)
                food_hit_list = arcade.check_for_collision_with_list(food, self.food_list)

                if len(wall_hit_list) == 0 and len(food_hit_list) == 0:
                    food_placed_successfully = True

            self.food_list.append(food)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        arcade.set_background_color(arcade.color.BLUE)

        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.player_list.draw()
        self.food_list.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        self.physics_engine.update()
        changed = False
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)
        if changed:

            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        self.food_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.food_list)
        for food in hit_list:
            food.remove_from_sprite_lists()
            self.score += 1



def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
