from PIL import Image, ImageDraw, ImageFont


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))


def get_text_color(rgb):
    brightness = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])
    return (255, 255, 255) if brightness < 128 else (0, 0, 0)


def draw_color_block(draw, hex_code, name, position, block_size):
    rgb = hex_to_rgb(hex_code)
    x_offset, y_offset = position
    block_width, block_height = block_size

    draw.rectangle([x_offset, y_offset, x_offset + block_width, y_offset + block_height], fill=rgb)

    text_color = get_text_color(rgb)
    text = f"{name} - {hex_code}"

    text_bbox = draw.textbbox((0, 0), text, font=ImageFont.load_default())
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_x = x_offset + (block_width - text_width) / 2
    text_y = y_offset + (block_height - text_height) / 2
    draw.text((text_x, text_y), text, fill=text_color, font=ImageFont.load_default())


def create_color_image(hex_list, names, max_blocks_per_row=7, block_size=(150, 100)):
    if len(hex_list) != len(names):
        raise ValueError("The number of hex codes must match the number of color names.")
    
    img_width = block_size[0] * max_blocks_per_row
    img_height = ((len(hex_list) + max_blocks_per_row - 1) // max_blocks_per_row) * block_size[1]

    img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    for i, (hex_code, name) in enumerate(zip(hex_list, names)):
        x_offset = (i % max_blocks_per_row) * block_size[0]
        y_offset = (i // max_blocks_per_row) * block_size[1]
        draw_color_block(draw, hex_code, name, (x_offset, y_offset), block_size)

    img.save('colors.png')


hex_list = [
    '#1a1a19', '#979796', '#868685', '#7d7d7c', '#d9d9d9',
    '#97d39a', '#A0F1B6', '#a6cded', '#8db4d4', '#7FBBB3', 
    '#85befd', '#94c9b2', '#7bb099', '#f7b4e1', '#ed557d',
    '#de9bc8', '#eb6f92', '#ffafa5', '#ef867c', '#cb6966',
    '#f4bf75', '#fd6853', '#ffdeaa', '#ffc591', '#d1d1d1'
]
names = [
    'Background', 'Comments', 'Grey3', 'invisibles', 'Foreground', 
    'green', 'green2', 'blue', 'blue2', 'blue3',
    'blue4', 'cyan', 'cyan2', 'magenta', 'crimson',
    'purple', 'pink', 'red', 'red2', 'red3', 
    'orange', 'orange2', 'yellow', 'yellow2', 'white'
]
create_color_image(hex_list, names, max_blocks_per_row=5, block_size=(150, 100))
