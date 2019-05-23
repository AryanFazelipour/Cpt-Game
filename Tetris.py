import arcade

# Set how many rows and columns we will have
ROW_COUNT = 18
COLUMN_COUNT = 22

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out oiur screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


grid = []



def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw the grid
    for row in range(18):
        for column in range(12):
            # Figure out what color to draw the box

            # Do the math to figure out where the box is
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

            # Draw the box
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, arcade.color.WHITE)

    arcade.draw_rectangle_filled(430, 235, 250, 500, arcade.color.BEIGE)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    global grid

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tetris")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    # array is simply a list of lists.
    for row in range(ROW_COUNT):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(COLUMN_COUNT):
            grid[row].append(0)  # Append a cell

    arcade.run()


if __name__ == '__main__':
    setup()