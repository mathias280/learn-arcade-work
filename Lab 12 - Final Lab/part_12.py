import arcade

SCREEN_HEIGHT = 950
SCREEN_WIDTH = 1000
SCREEN_TITLE = "Platform Game"

SPRITE_SCALING = 0.5

VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

TILE_SIZE = 64
SCALED_TILE_SIZE = TILE_SIZE * SPRITE_SCALING
MAP_HEIGHT = 10

MOVEMENT_SPEED = 6
JUMP_SPEED = 14
GRAVITY = 0.5
DIAMOND_AMOUNT = 6


def get_map_1():

    map_file = open("map2_floor.csv")

    map_array = []
    for line in map_file:
        line = line.strip()
        map_row = line.split(",")

        for index, item in enumerate(map_row):
            map_row[index] = int(item)

        map_array.append(map_row)
        map_file.close()

    return map_array


def get_map_2(map_array):

    map2_file = open("map2_door.csv")

    for line in map2_file:
        line = line.strip()
        map2_row = line.split(",")

        for index, item in enumerate(map2_row):
            map2_row[index] = int(item)

        map_array.append(map2_row)
        map2_file.close()

    return map_array


def get_map_3(map_array):

    map3_file = open("map2_background.csv")

    for line in map3_file:
        line = line.strip()
        map3_row = line.split(",")

        for index, item in enumerate(map3_row):
            map3_row[index] = int(item)

        map_array.append(map3_row)
        map3_file.close()

    return map_array


class TheGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.WHITE)

        self.player_list = None
        self.wall_list = None

        self.diamond_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0
        self.score = 0

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.diamond_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("Xavier.png", SPRITE_SCALING)

        self.player_sprite.center_x = 90
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        map_array = get_map_1("map2_floor.csv" "map2_door.csv", "map2_background.csv")

        for row_index in range(len(map_array)):
            for column_index in range(len(map_array[row_index])):

                item = map_array[row_index][column_index]

# items
                # -1 = empty
                # 11 = stonespike
                # 10 = door
                # 6 = stone
                # 9 = diamond

                wall = -1

                if item == 6:
                    wall = arcade.Sprite("stone.png", SPRITE_SCALING)
                elif item == 11:
                    wall = arcade.Sprite("stonespike.png", SPRITE_SCALING)
                elif item == 9:
                    wall = arcade.Sprite("diamond.png", SPRITE_SCALING)
                elif item == 10:
                    wall = arcade.Sprite("door.png", SPRITE_SCALING)

                if item >= 0:
                    wall.left = column_index * SCALED_TILE_SIZE
                    wall.top = (MAP_HEIGHT - row_index) * SCALED_TILE_SIZE

                    self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.player_list.draw()
        self.diamond_list.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


def on_key_press(self, key, modifiers):
    if key == arcade.key.SPACE:
        if self.physics_engine.can_jump():
            self.player_sprite.change_y = JUMP_SPEED
    elif key == arcade.key.A:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    elif key == arcade.key.D:
        self.player_sprite.change_x = MOVEMENT_SPEED


def on_key_release(self, key, modifiers):
    if key == arcade.key.A or key == arcade.key.D:
        self.player_sprite.change_x = 0


def on_update(self, delta_time):
    self.physics_engine.update()

    changed = False

    left_bndry = self.view_left + VIEWPORT_MARGIN
    if self.player_sprite.left < left_bndry:
        self.view_left -= left_bndry - self.player_sprite.left
        changed = True

    right_bndry = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
    if self.player_sprite.right > right_bndry:
        self.view_left += self.player_sprite.right - right_bndry
        changed = True

    top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
    if self.player_sprite.top > top_bndry:
        self.view_bottom += self.player_sprite.top - top_bndry
        changed = True

    bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
    if self.player_sprite.bottom < bottom_bndry:
        self.view_bottom -= bottom_bndry - self.player_sprite.bottom
        changed = True

    if changed:
        arcade.set_viewport(self.view_left,
                            SCREEN_WIDTH + self.view_left,
                            self.view_bottom,
                            SCREEN_HEIGHT + self.view_bottom)

    self.diamond_list.update()
    hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.diamond_list)
    for diamond in hit_list:
        diamond.remove_from_sprite_lists()
        self.score += 1


def main():
    window = TheGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
