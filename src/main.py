from PIL import Image
import process
from pathlib import Path

background = Image.open("../img/backgrounds/background_medieval.jpeg").convert("RGBA")
logo_skk = Image.open("../img/logos/logo_skk3d.png").convert("RGBA") 
logo_partner = Image.open("../img/logos/logo_lastsword.png").convert("RGBA")

directory_path = Path("../img/data")

for file_path in directory_path.rglob("*"):  # Usa "*.ext" para un tipo específico
    if file_path.is_file():
        image = Image.open(file_path)
        processed = process.process_image(image, background, logo_skk, logo_partner,file_path)
        #processed = process.add_logos(image, logo_skk, logo_partner)
        processed.save('../img/result/'+file_path.stem+".jpg", 'png')