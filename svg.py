import drawsvg as draw


class Canvas:
    def __init__(self, width, height, offset = 300, bg_color = "white"):
        self.offset = offset
        self.width = width + self.offset
        self.height = height + self.offset
        self.origin = (-(self.offset / 2), -(self.offset / 2))
        self.bg_color = bg_color
        self.initialize()

    def initialize(self):
        d = draw.Drawing(self.width, self.height, origin=self.origin)
        d.set_pixel_scale(3)
        d.append(draw.Rectangle(-self.offset/2, -self.offset/2, self.width, self.height, fill=self.bg_color))
        self.d = d

    def save(self, filename="example"):
        self.d.save_svg(f"{filename}.svg")
        self.d.save_png(f"{filename}.png")

    def draw_rectangle(self, x, y, width, height, stroke="black", stroke_width=8, fill="white"):
        self.d.append(draw.Rectangle(x, y, width, height, stroke=stroke, stroke_width=stroke_width, fill=fill))

    def arrow(self, x, y, lenght, direction, text=None, both_ends=True):
        directions = {"left": 0, "right": 180, "up": 90, "down": 270}

        transformation = f"rotate({directions[direction]}, {x}, {y})"
        text_rotate = -(directions[direction])

        arrow = draw.Group()
        arrow.append(draw.Line(x, y, x - lenght, y, stroke_width=3))
        arrow.append(
            draw.Lines(
                x - lenght,
                y,
                x - lenght + 15,
                y - 15,
                x - lenght + 15,
                y + 15,
                stroke_width=3,
            )
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
        self.d.append(
            draw.Use(arrow, 0, 0, stroke="black", fill="black", transform=transformation)
        )
        
