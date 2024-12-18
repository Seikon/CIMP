from rembg import remove
from PIL import Image
import io

def process_image(image, background, logo_left, logo_right):

    background = background.resize(image.size)

    output_image = remove(image)

    combined = Image.alpha_composite(background, output_image).convert("RGB")

    combined = add_logos(combined, logo_left, logo_right)

    return combined

def remove_background(image):

    output_image = remove(image)
    bg_removed = Image.open(io.BytesIO(output_image))
    return bg_removed

def add_logos(image, logo_left, logo_right):

    logo_size = (int(image.width * 0.15), int(image.height * 0.15))

    logo_left = logo_left.resize(logo_size)        
    logo_right = logo_right.resize(logo_size)

        # Crear un lienzo para combinar
    main_canvas = image.convert("RGBA")

    # Coordenadas para posicionar los logos en el tercio inferior
    margin = 50  # Espacio desde los bordes
    y_position = image.height - logo_left.height - margin

    # Posicionar el logo izquierdo
    x_left = margin
    main_canvas.paste(logo_left, (x_left, y_position), logo_left)

    # Posicionar el logo derecho
    x_right = image.width - logo_right.width - margin
    main_canvas.paste(logo_right, (x_right, y_position), logo_right)

    # Convertir a RGB si necesitas guardarlo como JPG
    image = main_canvas.convert("RGBA")

    return image