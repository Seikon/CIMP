from rembg import remove
from PIL import Image
import io


def add_logos(image, logo_left, logo_right):

    return image


background = Image.open("../img/background.jpg").convert("RGBA")
logo_skk = Image.open("../img/logos/logo_skk3d.jpg").convert("RGBA") 
logo_partner = Image.open("../img/logos/logo_kns.jpg").convert("RGBA") 

# Abrir la imagen original
with open('../img/data/payback-color-b.jpg', 'rb') as file:
    input_image = file.read()

background = background.resize(Image.open(io.BytesIO(input_image)).size)

# Remover el fondo
output_image = remove(input_image)

final = Image.open(io.BytesIO(output_image))

combined = Image.alpha_composite(background, final).convert("RGB")

# Añadir logos
combined = add_logos(combined, logo_skk, logo_partner)

combined.save('../img/result/output.jpg',"JPEG")