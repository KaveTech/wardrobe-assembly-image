from functools import cached_property


def get_body_position(wardrobe, body):
    return sum([wardrobe[i]["width"] for i in range(body)])


class Wardrobe:
    def __init__(self, wardrobe_json):
        self.body = []
        self.wardrobe = wardrobe_json
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

    @cached_property
    def width(self):
        return sum(
            [self.wardrobe[bodies]["width"] for bodies in range(len(self.wardrobe))]
        )

    @cached_property
    def height(self):
        return max(
            [self.wardrobe[bodies]["height"] for bodies in range(len(self.wardrobe))]
        )


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
        if position == 0:
            usable_width = body_width - (19 * 2) - 2
        else:
            usable_width = body_width - 30 - 2
        self.canvas.arrow(position, body_height + 50, body_width, "right", usable_width)

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
        self.set_component_number_in_body()
        self.set_component_index_in_body()
        self.set_components_parameters()
        self.set_component_text_position()

    def set_component_number_in_body(self):
        for component in self.components:
            body = self.components[component]["body"]
            self.components[component]["number_in_body"] = len(
                [i for i in self.components if self.components[i]["body"] == body]
            )

    def set_component_index_in_body(self):
        for component in self.components:
            body = self.components[component]["body"]
            self.components[component]["index_in_body"] = [
                i for i in self.components if self.components[i]["body"] == body
            ].index(component) + 1

    def set_components_parameters(self):
        for component in self.components:
            body = self.components[component]["body"]
            self.components[component]["position"] = self.wardrobe.position(body)
            self.components[component]["width"] = self.wardrobe.body_width(body)
            self.components[component]["height_in_vector"] = (
                self.wardrobe.bottom - self.components[component]["height"]
            )

    def set_component_text_position(self):
        for component in self.components:
            width = self.components[component]["width"]
            number_in_body = self.components[component]["number_in_body"]
            index_in_body = self.components[component]["index_in_body"]
            to_add = width / (number_in_body + 1) * index_in_body
            if number_in_body == 1:
                text_position = self.components[component]["position"] + width / 2
            else:
                text_position = self.components[component]["position"] + to_add
            self.components[component]["text_position"] = text_position


class ComponentConstructor:
    def __init__(self, canvas, components):
        self.canvas = canvas
        self.components = components.components
        self.component_builder = {
            "shelf": self.draw_shelf,
            "drawer": self.draw_drawer,
        }

    def draw_component_dimensions(
        self, position, width, component_height_in_vector, component_height
    ):
        self.canvas.arrow(
            position,
            component_height_in_vector + 20,
            component_height - 40,
            "down",
            component_height,
        )

    def draw_shelf(self, width, component_height, position):
        self.canvas.draw_rectangle(position, component_height, width, -30, fill="gray")

    def draw_drawer(self, width, component_height, position):
        self.canvas.draw_rectangle(
            position, component_height, width, -300, fill="brown"
        )

    def draw_component(self, component):
        self.component_builder[component["component"]](
            component["width"],
            component["height_in_vector"],
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
                component["text_position"],
                component["width"],
                component["height_in_vector"],
                component["height"],
            )
