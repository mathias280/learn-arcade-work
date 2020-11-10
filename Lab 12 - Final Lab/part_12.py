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


def get_map(pmap, pmap_layer1):
    map_file = open(pmap.csv)

    map_array = []
    for line in map_file:
        line = line.strip()
        map_row = line.split(",")

        for i in range(len(map_row)):
            map_row[i] = int(map_row[i])

        map_array.append(map_row)

    return map_array

    # map_file2 = open(pmap_layer1.cvs)
    # for line in map_file2:
    # line = line.strip()
    # map_row = line.split(",")
    # for index, item in enumerate(map_row):
    # map_row[index] = int(item)
    # map_array.append(map_row)


class TheGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.NAVY_BLUE)

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING)

        self.player_sprite.center_x = 90
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)
        map_array = []
        for row_index in range(len(map_array)):
            for column_index in range(len(map_array[row_index])):

                item = map_array[row_index][column_index]

                # -1 = empty
                # 0 = snow
                # 1 = snowrock
                # 3 = stonespike
                # 4 = door
                # 6 = stone

                if item == 0:
                    wall = arcade.Sprite("snow.png", SPRITE_SCALING)
                elif item == 1:
                    wall = arcade.Sprite("snowrock.png", SPRITE_SCALING)
                elif item == 3:
                    wall = arcade.Sprite("stonespike.png", SPRITE_SCALING)
                elif item == 4:
                    wall = arcade.Sprite("door.png", SPRITE_SCALING)
                elif item == 6:
                    wall = arcade.Sprite("stone.png", SPRITE_SCALING)

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


def on_key_press(self, key, modifiers):
    if key == arcade.key.UP:
        if self.physics_engine.can_jump():
            self.player_sprite.change_y = JUMP_SPEED
    elif key == arcade.key.LEFT:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = MOVEMENT_SPEED


def on_key_release(self, key, modifiers):
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        self.player_sprite.change_x = 0


def update(self, delta_time):
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


def main():
    window = TheGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
