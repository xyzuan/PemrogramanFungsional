from PIL import Image, ImageEnhance
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(current_dir, "img", "202110370311147.jpg")

image = Image.open(image_path)

brightness_enhancer = ImageEnhance.Brightness(image)
brightened = brightness_enhancer.enhance(1.5)

contrast_enhancer = ImageEnhance.Contrast(brightened)
final = contrast_enhancer.enhance(1.2)

output_dir = os.path.join(current_dir, "img", "output")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "kegiatan3.png")

final.save(output_path)
final.show()