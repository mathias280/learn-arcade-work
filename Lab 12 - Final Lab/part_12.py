"""
Platformer Game
Enjoy!
"""
import arcade
# import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer Game"

CHARACTER_SCALING = 0.7
TILE_SCALING = 1.1
DIAMOND_SCALING = 0.4
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

PLAYER_MOVEMENT_SPEED = 8
GRAVITY = 1
PLAYER_JUMP_SPEED = 17

LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 64
PLAYER_START_Y = 225


class OpeningView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.BLACK)

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        arcade.start_render()
        arcade.draw_text("Game Start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.csscolor.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.csscolor.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, button, modifiers):
        game_view = MyGame()
        game_view.setup_level1()
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    def on_draw(self):
        arcade.set_background_color(arcade.csscolor.BLACK)

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        arcade.start_render()
        arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.csscolor.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("No More Lives", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.csscolor.WHITE, font_size=40, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyGame()
        game_view.setup_level1()
        self.window.show_view(game_view)


class MyGame(arcade.View):

    def __init__(self):

        super().__init__()

        self.diamond_list = None
        self.wall_list = None
        # self.foreground_list = None
        # self.background_list = None
        self.danger_list = None
        self.player_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.view_bottom = 0
        self.view_left = 0

        self.score = 0

        self.player_lives = 5

        self.end_of_map = 0

        self.level = 1

        # Sounds
        self.collect_diamond_sound = arcade.load_sound("coin2.wav")
        self.jump_sound = arcade.load_sound("jump3.wav")
        self.game_over = arcade.load_sound("gameover4.wav")

    def life_counter(self):

        self.player_lives = 0

    def setup_level1(self):

        self.view_bottom = 0
        self.view_left = 0

        self.score = 0

        self.player_list = arcade.SpriteList()
        # self.foreground_list = arcade.SpriteList()
        # self.background_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.diamond_list = arcade.SpriteList()

        image_source = "Xavier.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        # --- Load in a map from the tiled ---

        platforms_layer_name = 'Platforms'
        moving_platforms_layer_name = 'Moving Platforms'
        diamonds_layer_name = 'Diamonds'
        # foreground_layer_name = 'Foreground'
        # background_layer_name = 'Background'
        danger_layer_name = "Danger"

        map_name = f"map3.tmx"

        my_map = arcade.tilemap.read_tmx(map_name)

        self.end_of_map = my_map.map_size.width * GRID_PIXEL_SIZE

        # self.background_list = arcade.tilemap.process_layer(my_map,
        # background_layer_name,
        # TILE_SCALING)

        # self.foreground_list = arcade.tilemap.process_layer(my_map,
        # foreground_layer_name,
        # TILE_SCALING)

        # moving_platforms_list = arcade.tilemap.process_layer(my_map, moving platforms_layer_name, TILE_SCALING)
        # for sprite in moving_platforms_list:
        # self.wall_list.append(sprite)

        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)

        self.diamond_list = arcade.tilemap.process_layer(my_map,
                                                         diamonds_layer_name,
                                                         TILE_SCALING,
                                                         use_spatial_hash=True)

        self.danger_list = arcade.tilemap.process_layer(my_map,
                                                        danger_layer_name,
                                                        TILE_SCALING,
                                                        use_spatial_hash=True)

        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def setup_level2(self):

        self.view_bottom = 0
        self.view_left = 0

        # self.foreground_list = arcade.SpriteList()
        # self.background_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.diamond_list = arcade.SpriteList()

        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y

        # --- Load in a map from the tiled ---

        platforms_layer_name = 'Platforms'
        moving_platforms_layer_name = 'Moving Platforms'
        diamonds_layer_name = 'Diamonds'
        # foreground_layer_name = 'Foreground'
        # background_layer_name = 'Background'
        danger_layer_name = "Danger"

        map_name = f"map4.tmx"

        my_map = arcade.tilemap.read_tmx(map_name)

        self.end_of_map = my_map.map_size.width * GRID_PIXEL_SIZE

        # self.background_list = arcade.tilemap.process_layer(my_map,
        # background_layer_name,
        # TILE_SCALING)

        # self.foreground_list = arcade.tilemap.process_layer(my_map,
        # foreground_layer_name,
        # TILE_SCALING)

        # moving_platforms_list = arcade.tilemap.process_layer(my_map, moving platforms_layer_name, TILE_SCALING)
        # for sprite in moving_platforms_list:
        # self.wall_list.append(sprite)

        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)

        self.diamond_list = arcade.tilemap.process_layer(my_map,
                                                         diamonds_layer_name,
                                                         TILE_SCALING,
                                                         use_spatial_hash=True)

        self.danger_list = arcade.tilemap.process_layer(my_map,
                                                        danger_layer_name,
                                                        TILE_SCALING,
                                                        use_spatial_hash=True)

        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        # self.background_list.draw()
        self.wall_list.draw()
        self.diamond_list.draw()
        self.danger_list.draw()
        self.player_list.draw()
        # self.foreground_list.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)

        lives_text = f"Lives: {self.player_lives}"
        arcade.draw_text(lives_text, 30 + self.view_left, 30 + self.view_bottom, arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):

        self.physics_engine.update()

        diamond_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.diamond_list)
        for diamond in diamond_hit_list:
            diamond.remove_from_sprite_lists()
            arcade.play_sound(self.collect_diamond_sound)
            self.score += 1

        changed_viewport = False

        # for wall in self.wall_list:

        # if wall.boundary_right and wall.right > wall.boundary_right and wall.change_x > 0:
        # wall.change_x *= -1
        # if wall.boundary_left and wall.left < wall.boundary_left and wall.change_x < 0:
        # wall.change_x *= -1
        # if wall.boundary_top and wall.top > wall.boundary_top and wall.change_y > 0:
        # wall.change_y *= -1
        # if wall.boundary_bottom and wall.bottom < wall.boundary_bottom and wall.change_y < 0:
        # wall.change_y *= -1

        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True
            arcade.play_sound(self.game_over)

        if arcade.check_for_collision_with_list(self.player_sprite,
                                                self.danger_list):
            self.player_lives -= 1

            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True
            arcade.play_sound(self.game_over)

        print(self.player_sprite.center_x)

        if self.player_sprite.center_x >= 3870:
            self.level += 1

            self.setup_level2()

            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True

        if self.player_lives <= 0:
            view = GameOverView()
            self.window.show_view(view)

        # --- Manage Scrolling ---

        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed_viewport = True

        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed_viewport = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed_viewport = True

        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed_viewport = True

        if changed_viewport:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = OpeningView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
