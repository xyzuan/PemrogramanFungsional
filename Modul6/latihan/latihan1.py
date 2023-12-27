from PIL import Image, ImageOps, ImageDraw, ImageFont
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(current_dir, "img", "202110370311147.jpg")
img = Image.open(img_path)

font_path = os.path.join(current_dir, "font", "arial_bold.ttf")
custom_font = ImageFont.truetype(font_path, 24)

img_after = ImageOps.grayscale(img.copy())
draw = ImageDraw.Draw(img_after)

text = "Jody Yuantoro, 202110370311147"
image_width, image_height = img.size

text_width, text_height = draw.textsize(text, font=custom_font)
text_position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
draw.text(text_position, text, font=custom_font, fill="white")

output_dir = os.path.join(current_dir, "output",)
output_path = os.path.join(output_dir, "kegiatan1.jpg")

img_after.save(output_path)
img_after.show()