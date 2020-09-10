import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def moon(x,y):
    """Draw the Moon """
    arcade.draw_lrtb_rectangle_filled(x, y, 100, 0, arcade.color.DARK_GRAY)


def obj(x,y):
    # Draw Object
    arcade.draw_ellipse_filled(x, 80, 60, 80, arcade.color.BATTLESHIP_GREY)

    arcade.draw_ellipse_filled(x, 20, 100, 20, arcade.color.BATTLESHIP_GREY)


def spaceship(x,y):
    # Draw Space ship
    arcade.draw_ellipse_filled(x, y, 100, 35, arcade.color.CADET_GREY)

    if (on_draw.space_x % 2 == 1 ):
        arcade.draw_ellipse_outline(400, 270, 70, 20, arcade.color.WHITE)

        arcade.draw_ellipse_outline(400, 240, 100, 20, arcade.color.WHITE)
    else:
        arcade.draw_ellipse_outline(400, 270, 70, 20, arcade.color.NAVY_BLUE)

        arcade.draw_ellipse_outline(400, 240, 100, 20, arcade.color.NAVY_BLUE)

    arcade.draw_ellipse_outline(400, 300, 101, 36, arcade.color.YELLOW)

    arcade.draw_ellipse_filled(x+1, y+18, 50, 15, arcade.color.SILVER)


def sun(x,y):
    # Draw Sun
    arcade.draw_circle_filled(x, y, 120, arcade.color.ORANGE_RED, 100)

    arcade.draw_circle_filled(x, y, 110, arcade.color.RED, 100)

    arcade.draw_circle_filled(x, y, 100, arcade.color.ORANGE_RED, 100)

    arcade.draw_circle_filled(x, y, 90, arcade.color.RED, 100)

    arcade.draw_circle_filled(x, y, 80, arcade.color.ORANGE_RED, 100)

    arcade.draw_circle_filled(x, y, 70, arcade.color.RED, 100)

    arcade.draw_circle_filled(x, y, 60, arcade.color.ORANGE_RED, 100)

    arcade.draw_circle_filled(x, y, 50, arcade.color.RED, 100)


def draw():
    # --- Finish drawing ---
    arcade.finish_render()


def run():
    # Keep the window up until someone closes it.
    arcade.run()


def on_draw(delta_time):
    arcade.start_render()

    # draws the moon
    moon(0, 800)
    obj(on_draw.obj_x, 150)
    spaceship(400, 300)
    sun(80, 400)

    on_draw.obj_x -= 2
    on_draw.space_x += 1

on_draw.obj_x = 514
on_draw.space_x = 0

def main():
    arcade.open_window(800, 600, "Drawing Example")

    # Set Background
    arcade.schedule(on_draw, 1/30)
    arcade.set_background_color(arcade.color.NAVY_BLUE)




    #run function
    run()




main()