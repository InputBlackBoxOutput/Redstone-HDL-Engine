class Contraption:
    def __init__(self):
        self.render_distance = 1  # 12  # Default for 64-bit computers
        self.chunk_size = 16  # Blocks
        self.width = self.render_distance * self.chunk_size
        self.height = self.render_distance * self.chunk_size

        self.air = "air"
        self.light_gray_concrete = "light_gray_concrete"
        self.light_green_concrete = "lime_concrete"

        self.redstone_block = "redstone_block"
        self.redstone_dust = "redstone"
        self.redstone_torch = "redstone_torch"
        self.redstone_lamp = "redstone_lamp"
        self.redstone_switch = "lever"

        self.canvas = self.create_minecraft_canvas()

    # Refactor according to minecraft coordinates:
    # Current -> (16 x 12) * (16 x 12) * (16) & Layer one is light gray concrete
    def create_minecraft_canvas(self):
        canvas = []

        for i in range(self.height):
            canvas.append([])
            for j in range(self.width):
                canvas[i].append([])
                for k in range(self.chunk_size):
                    if i != 0:
                        canvas[i][j].append(self.air)
                    else:
                        canvas[i][j].append(self.light_gray_concrete)

        return canvas

    def place_port(self, coordinates):
        pass

    def place_nport(self, coordinates):
        pass

    def place_and(self, coordinates):
        pass

    def place_nand(self, coordinates):
        pass

    def place_logic1(self, coordinates):
        pass

    def place_logic0(self, coordinates):
        pass

    def show_canvas(self):
        print(self.canvas[:2])


class ContraptionDiagram:
    def __init__(self):
        self.height = 10
        self.width = 10

        self.air = ' '
        self.light_gray_concrete = "#"

        self.redstone_block = "@"
        self.redstone_dust = "-"
        self.redstone_torch = "="
        self.redstone_lamp = "*"
        self.redstone_switch = "]"

        self.canvas = self.create_minecraft_canvas()

    def create_minecraft_canvas(self):
        canvas = []

        for i in range(self.height):
            canvas.append([])
            for j in range(self.width):
                canvas[i].append(' ')

        return canvas

    def place_port(self, coordinates):
        self.canvas[coordinates[0]][coordinates[1]] = "!"

    def place_nport(self, coordinates):
        self.canvas[coordinates[0]][coordinates[1]] = "!"

    def place_and(self, coordinates):
        self.canvas[coordinates[0]][coordinates[1]] = "!"

    def place_nand(self, coordinates):
        self.canvas[coordinates[0]][coordinates[1]] = "!"

    def place_logic1(self, coordinates):
        self.canvas[coordinates[0]][coordinates[1]] = "!"

    def place_logic0(self, coordinates):
        self.canvas[coordinates[0]][coordinates[1]] = "!"

    def show_canvas(self):
        for i in range(self.height):
            print("".join(self.canvas[i]))


if __name__ == "__main__":
    # c = Contraption()
    # c.show_canvas()

    c = ContraptionDiagram()
    c.place_port((0, 3))
    c.show_canvas()
