from PIL import Image
from PIL import ImageDraw


def draw_map(map_content, map_width, map_height, obstacle_character, final_output, starting_position_x, starting_position_y):
    map_tab = map_content.splitlines()
    final_output_tab = stock_final_output(final_output, starting_position_x, starting_position_y)
    width_counter = 0
    height_counter = 0
    height_position = 0
    width_position = 0
    final_image = Image.new('RGB', (1280, 720), (255, 255, 255))
    draw = ImageDraw.Draw(final_image)
    while height_counter < map_height:
        while width_counter < map_width:
            if map_tab[height_counter][width_counter] == obstacle_character:
                draw.rectangle(((width_position, height_position), (width_position + 60, height_position + 60)), fill='yellow', outline='black')
                draw.line((width_position, height_position, width_position + 60, height_position + 60), fill='red', width=2)
            elif (height_counter == starting_position_y and starting_position_x == width_counter) or check_final_input(final_output_tab, height_counter, width_counter):
                draw.rectangle(((width_position, height_position), (width_position + 60, height_position + 60)), fill='green', outline='black')
            else:
                draw.rectangle(((width_position, height_position), (width_position + 60, height_position + 60)), fill='yellow', outline='black')

            width_position += 60
            width_counter += 1
        width_position = 0
        width_counter = 0
        height_counter += 1
        height_position += 60

    final_image.show()


def stock_final_output(final_output, starting_x, starting_y):
    final_res = [] * len(final_output)
    counter = 1
    final_res.append((starting_x, starting_y))
    for c in final_output:
        if c == 'R':
            starting_x += 1
        if c == 'L':
            starting_x -= 1
        if c == 'B':
            starting_y += 1
        if c == 'T':
            starting_y -= 1
        final_res.append((starting_x, starting_y))
        counter += 1
    return tuple(final_res)


def check_final_input(final_output_tab, height_counter, width_counter):
    for pos in range(len(final_output_tab)):
        if final_output_tab[pos][0] == width_counter and final_output_tab[pos][1] == height_counter:
            return True
    return False
