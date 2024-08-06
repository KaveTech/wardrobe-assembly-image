import json
import os
import drawsvg as draw

file_name = "webhook.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, file_name)

with open(file_path, "r") as file:
    data = json.load(file)
    print(len(data['order']['lines']))

wardrobe_json = {}

for i in range(len(data['order']['lines'])):
    if data['order']['lines'][i]['product_classification'] == 'wardrobe_body_extension' or data['order']['lines'][i]['product_classification'] == 'wardrobe_body_base':
        design_module_index = data['order']['lines'][i]['customisation_details']['design_module_index'] - 1
        wardrobe_json[design_module_index] = {
            "width": data['order']['lines'][i]['customisation_details']['width'],
            "height": data['order']['lines'][i]['customisation_details']['height'],
        }

print(wardrobe_json)

components_json = {}

for i in range(len(data['order']['lines'])):
    if data['order']['lines'][i]['product_classification'] == 'wardrobe_shelf':
        design_module_index = data['order']['lines'][i]['customisation_details']['design_module_index'] - 1
        components_json[design_module_index] = {
            "body": design_module_index,
            "component": "shelf",
            "height": data['order']['lines'][i]['customisation_details']['assembly_position_Y'],
        }

print(components_json)

# Define arrow function
def arrow(x, y, lenght, direction, text=None, both_ends=True):
    directions = {"left": 0, "right": 180, "up": 90, "down": 270}

    transformation = f"rotate({directions[direction]}, {x}, {y})"
    text_rotate = -(directions[direction])

    arrow = draw.Group()
    arrow.append(draw.Line(x, y, x - lenght, y, stroke_width=3))
    arrow.append(
        draw.Lines(x - lenght, y, x - lenght + 15, y - 15, x - lenght + 15, y + 15, stroke_width=3)
    )
    if both_ends:
        arrow.append(draw.Lines(x, y, x - 15, y - 15, x - 15, y + 15, stroke_width=3))
    if text:
        arrow.append(
            draw.Text(
                str(text),
                x=x - lenght / 2,
                y=y,
                font_size=50,
                text_anchor="middle",
                transform=f"rotate({text_rotate},{x - lenght / 2}, {y})",
            )
        )
    d.append(
        draw.Use(arrow, 0, 0, stroke="black", fill="black", transform=transformation)
    )


""" wardrobe_json = {
    0: {"width": 100, "height": 200},
    1: {"width": 100, "height": 200},
    2: {"width": 100, "height": 200},
    3: {"width": 100, "height": 200},
}

components_json = {
    0: {"body": 0, "component": "shelf", "height": 130},
    1: {"body": 0, "component": "shelf", "height": 150},
    2: {"body": 1, "component": "shelf", "height": 130},
    3: {"body": 2, "component": "shelf", "height": 130},
} """


""" wardrobe_json = {
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
} """


def get_wardrobe_width(wardrobe):
    return sum([wardrobe[i]["width"] for i in range(len(wardrobe))])


def get_wardrobe_height(wardrobe):
    return max([wardrobe[i]["height"] for i in range(len(wardrobe))])


def get_body_position(wardrobe, body):
    return sum([wardrobe[i]["width"] for i in range(body)])


class Wardrobe:
    def __init__(self, wardrobe_json):
        self.body = []
        self.wardrobe = wardrobe_json
        self.width = get_wardrobe_width(self.wardrobe)
        self.height = get_wardrobe_height(self.wardrobe)

    def set_bodies_position(self):
        for body in self.wardrobe:
            self.body.append(
                {
                    "width": self.wardrobe[body]["width"],
                    "height": self.wardrobe[body]["height"],
                    "position": get_body_position(self.wardrobe, body),
                }
            )

    def body_width(self, body):
        return self.body[body]["width"]

    def body_height(self, body):
        return self.body[body]["height"]

    def position(self, body):
        return self.body[body]["position"]


class WardrobeConstructor:
    def __init__(self, wardrobe):
        self.wardrobe = wardrobe

    def draw_body(self, d, body):
        body_width = self.wardrobe.body_width(body)
        body_height = self.wardrobe.body_height(body)
        position = self.wardrobe.position(body)
        b = draw.Rectangle(
            position,
            0,
            body_width,
            body_height,
            stroke="black",
            stroke_width=8,
            fill="white",
        )
        d.append(b)

    def draw_all_bodies(self, d):
        for body in range(len(self.wardrobe.body)):
            self.draw_body(d, body)
            arrow(
                self.wardrobe.position(body),
                self.wardrobe.body_height(body) + 50,
                self.wardrobe.body_width(body),
                "right",
                self.wardrobe.body_width(body),
            )


class Components:
    def __init__(self, wardrobe, components_json):
        self.components = components_json
        self.wardrobe = wardrobe

    def set_components_positions(self):
        for component in self.components:
            body = self.components[component]["body"]
            component_position = self.wardrobe.position(body)
            self.components[component]["position"] = component_position

    def set_component_width(self):
        for component in self.components:
            body = self.components[component]["body"]
            self.components[component]["width"] = self.wardrobe.body_width(body)

    def get_components(self):
        return self.components


class ComponentConstructor:
    def __init__(self, components, wardrobe):
        self.components = components.components
        self.wardrobe = wardrobe
        self.component_builder = {"shelf": self.draw_shelf}

    def draw_shelf(self, width, component_height, position, d):
        wardrobe_bottom = self.wardrobe.height
        component_height_canvas = wardrobe_bottom - component_height
        shelf = draw.Rectangle(
            position,
            component_height_canvas,
            width,
            30,
            stroke="black",
            stroke_width=6,
            fill="gray",
        )
        d.append(shelf)
        arrow(position + width / 2, component_height_canvas + 250, 200, "up", component_height, False)

    def draw_component(self, d, component):
        component_type = self.components[component]["component"]
        component_position = self.components[component]["position"]
        component_height = self.components[component]["height"]
        self.component_builder[component_type](
            self.components[component]["width"], component_height, component_position, d
        )

    def draw_all_components(self, d):
        for component in self.components:
            self.draw_component(d, component)


wardrobe = Wardrobe(wardrobe_json)
wardrobe.set_bodies_position()
wardrobe_constructor = WardrobeConstructor(wardrobe)
components = Components(wardrobe, components_json)
components.set_components_positions()
components.set_component_width()
components_constructor = ComponentConstructor(components, wardrobe)

# Set up canvas
DRAWING_OFFSET = 300
TOTAL_WARDROBE_WIDTH = wardrobe.width
TOTAL_WARDROBE_HEIGHT = wardrobe.height
BACKGROUND_COLOR = "white"
DRAWING_ORIGIN = (-(DRAWING_OFFSET / 2), -(DRAWING_OFFSET / 2))

d = draw.Drawing(
    TOTAL_WARDROBE_WIDTH + DRAWING_OFFSET,
    TOTAL_WARDROBE_HEIGHT + DRAWING_OFFSET,
    origin=DRAWING_ORIGIN,
)
d.append(
    draw.Rectangle(
        -(DRAWING_OFFSET / 2),
        -(DRAWING_OFFSET / 2),
        TOTAL_WARDROBE_WIDTH + DRAWING_OFFSET,
        TOTAL_WARDROBE_HEIGHT + DRAWING_OFFSET,
        fill=BACKGROUND_COLOR,
    )
)


# Draw wardrobe and components
wardrobe_constructor.draw_all_bodies(d)
components_constructor.draw_all_components(d)


# Draw total wardrobe width and height arrows
arrow(0, -50, TOTAL_WARDROBE_WIDTH, "right", TOTAL_WARDROBE_WIDTH)
arrow(-80, 0, TOTAL_WARDROBE_HEIGHT, "down", TOTAL_WARDROBE_HEIGHT)


d.set_pixel_scale(3)  # Set number of pixels per geometry unit
d.save_svg("example.svg")
d.save_png("example.png")
