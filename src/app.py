from PIL import Image
import process
from pathlib import Path
import dearpygui.dearpygui as dpg
from constants import *


def create_image_container():
    with dpg.group(horizontal=False):

        image_path = "../img/data/elf-rogue.jpg"

        width, height, channels, data = dpg.load_image(image_path)

        with dpg.texture_registry(show=False):
            dpg.add_dynamic_texture(width=width, height=height, default_value=data, tag=TEXTURE_TAG)

        dpg.add_image(TEXTURE_TAG)

dpg.create_context()

with dpg.window(tag="Primary Window", width=600, height=820):
    create_image_container()

dpg.create_viewport(title='Generacion de imagenes de catalogo', width=600, height=820)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()