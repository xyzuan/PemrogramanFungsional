from PIL import Image
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

background_path = os.path.join(current_dir, "img", "202110370311147.jpg")
overlay_path = os.path.join(current_dir, "img", "Logo_umm.png")

background = Image.open(background_path)
overlay = Image.open(overlay_path)
overlay = overlay.convert("RGBA")
overlay = overlay.resize((180, 180))

x_position = 125
y_position = 125
background.paste(overlay, (x_position, y_position), overlay)

output_dir = os.path.join(current_dir, "img", "output")
output_path = os.path.join(output_dir, "kegiatan2.png")

os.makedirs(output_dir, exist_ok=True)

background.save(output_path)
background.show()