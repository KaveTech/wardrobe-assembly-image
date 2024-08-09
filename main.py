import os
import json

from svg import Canvas
from assembly_image import Wardrobe
from assembly_image import WardrobeConstructor
from assembly_image import Components
from assembly_image import ComponentConstructor

from translator import get_wardrobe
from translator import get_components

modular_design_code = input("Enter the modular design code: ")
if "MD-" not in modular_design_code:
    modular_design_code = f"MD-{modular_design_code}"

file_name = f"{modular_design_code}.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, file_name)

with open(file_path, "r") as file:
    data = json.load(file)


wardrobe_json = get_wardrobe(data)
components_json = get_components(data)

wardrobe = Wardrobe(wardrobe_json)
canvas = Canvas(wardrobe.width, wardrobe.height)

wardrobe_constructor = WardrobeConstructor(canvas, wardrobe)
components = Components(wardrobe, components_json)
components_constructor = ComponentConstructor(canvas, components)

wardrobe_constructor.draw_wardrobe_dimensions()
wardrobe_constructor.draw_all_bodies()
wardrobe_constructor.draw_all_bodies_dimensions()
components_constructor.draw_all_components()
components_constructor.draw_all_components_dimensions()

canvas.save(modular_design_code)