from svg import Canvas
from assembly_image import Wardrobe
from assembly_image import WardrobeConstructor
from assembly_image import Components
from assembly_image import ComponentConstructor


wardrobe_json = {
    0: {"width": 700, "height": 2000},
    1: {"width": 600, "height": 2000},
    2: {"width": 1400, "height": 2000},
    3: {"width": 500, "height": 2000},
    4: {"width": 500, "height": 2000},
}

components_json = {
    0: {"body": 0, "component": "shelf", "height": 800},
    1: {"body": 0, "component": "shelf", "height": 1200},
    2: {"body": 1, "component": "shelf", "height": 1300},
    3: {"body": 2, "component": "shelf", "height": 400},
    4: {"body": 2, "component": "shelf", "height": 600},
    5: {"body": 3, "component": "shelf", "height": 1600},
    6: {"body": 4, "component": "shelf", "height": 1600},
}


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

canvas.save("MD-000001")