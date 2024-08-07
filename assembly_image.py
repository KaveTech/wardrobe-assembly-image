

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
        self.bottom = self.height
        self.set_bodies_position()

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
    def __init__(self, canvas, wardrobe):
        self.canvas = canvas
        self.wardrobe = wardrobe

    def draw_wardrobe_dimensions(self):
        self.canvas.arrow(0, -50, self.wardrobe.width, "right", self.wardrobe.width)
        self.canvas.arrow(-80, 0, self.wardrobe.height, "down", self.wardrobe.height)

    def draw_body_dimensions(self, body):
        body_width = body["width"]
        body_height = body["height"]
        position = body["position"]
        self.canvas.arrow(position, body_height + 50, body_width, "right", body_width)

    def draw_body(self, body):
        body_width = body["width"]
        body_height = body["height"]
        position = body["position"]
        self.canvas.draw_rectangle(position, 0, body_width, body_height)

    def draw_all_bodies(self):
        for body_position in range(len(self.wardrobe.body)):
            body = self.wardrobe.body[body_position]
            self.draw_body(body)

    def draw_all_bodies_dimensions(self):
        for body_position in range(len(self.wardrobe.body)):
            body = self.wardrobe.body[body_position]
            self.draw_body_dimensions(body)


class Components:
    def __init__(self, wardrobe, components_json):
        self.components = components_json
        self.wardrobe = wardrobe
        self.set_components_parameters()

    def set_components_parameters(self):
        for component in self.components:
            body = self.components[component]["body"]
            component_position = self.wardrobe.position(body)
            self.components[component]["position"] = component_position
            self.components[component]["width"] = self.wardrobe.body_width(body)
            self.components[component]["height"] = (
                self.wardrobe.bottom - self.components[component]["height"]
            )


class ComponentConstructor:
    def __init__(self, canvas, components):
        self.canvas = canvas
        self.components = components.components
        self.component_builder = {"shelf": self.draw_shelf}

    def draw_component_dimensions(self, position, width, component_height):
        self.canvas.arrow(
            position + width / 2,
            component_height + 250,
            200,
            "up",
            component_height,
            False,
        )

    def draw_shelf(self, width, component_height, position):
        self.canvas.draw_rectangle(position, component_height, width, 30, fill="gray")

    def draw_component(self, component):
        self.component_builder[component["component"]](
            component["width"],
            component["height"],
            component["position"],
        )

    def draw_all_components(self):
        for item in self.components:
            component = self.components[item]
            self.draw_component(component)

    def draw_all_components_dimensions(self):
        for item in self.components:
            component = self.components[item]
            self.draw_component_dimensions(
                component["position"], component["width"], component["height"]
            )