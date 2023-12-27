from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

background = Image.open(os.path.join(current_dir, "img", "umm_bg.jpeg"))
overlay = Image.open(os.path.join(current_dir, "img", "umm_logo.jpeg"))
fontPath = os.path.join(current_dir, "font", "arial_bold.ttf")

grayscale = ImageOps.grayscale(background.copy())
rotate = grayscale.rotate(30)
blurredBg = rotate.filter(ImageFilter.BLUR)
finalBg = blurredBg.resize((1980, 1080))

overlayEncB = ImageEnhance.Brightness(overlay)
overlayBrightened = overlayEncB.enhance(1.47)

overlayEncC = ImageEnhance.Contrast(overlayBrightened)
overlayContrasted = overlayEncC.enhance(1.47)

finalEnc = overlayContrasted.resize((500, 500))

padding = 170
customFont = ImageFont.truetype(fontPath, 24)
draw = ImageDraw.Draw(finalEnc)
text = "INFORMATIKA JOSSS!"
text_width, text_height = draw.textsize(text, font=customFont)
text_position = ((finalEnc.width - text_width) // 2, finalEnc.height - text_height - padding)
draw.text(text_position, text, font=customFont, fill="black")

overlay_position = (
    (finalBg.width - finalEnc.width) // 2,
    (finalBg.height - finalEnc.height) // 2
)

finalBg.paste(finalEnc, overlay_position)

output_dir = os.path.join(current_dir, "output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "tugas_praktikum_enam.jpg")

finalBg.save(output_path)
finalBg.show()
