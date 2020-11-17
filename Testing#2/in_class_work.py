# Might have to use
def __init__(self):
    """ This is run once when we switch to this view """
    super().__init__()
    # self.texture = arcade.load_texture("game_over.png")

    arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)


def on_draw(self):
    """ Draw this view """
    arcade.start_render()
    self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                            SCREEN_WIDTH, SCREEN_HEIGHT)
