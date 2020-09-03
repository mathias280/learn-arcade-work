import arcade

arcade.open_window(800, 600, "Drawing Example")
# Set Background
arcade.set_background_color(arcade.color.NAVY_BLUE)

arcade.start_render()

# Draw Moon
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_GRAY)

# Draw Object
arcade.draw_ellipse_filled(550, 80, 60, 80, arcade.color.BATTLESHIP_GREY)

arcade.draw_ellipse_filled(580, 20, 100, 20, arcade.color.BATTLESHIP_GREY)

# Draw Space ship
arcade.draw_ellipse_filled(400, 300, 100, 35, arcade.color.CADET_GREY)

arcade.draw_ellipse_filled(401, 318, 50, 15, arcade.color.CADET_GREY)

# Draw Sun
arcade.draw_circle_filled(80, 400, 120, arcade.color.ORANGE_RED, 100)

arcade.draw_circle_filled(80, 400, 100, arcade.color.RED, 100)


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()