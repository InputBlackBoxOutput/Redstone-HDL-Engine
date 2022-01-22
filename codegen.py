

class CodeGenerator:
	def __init__(self):
		self.render_distance = 12 # Default for 64-bit computers
		self.chunk_size = 16
		
		self.air = "minecraft:air"
		self.light_gray_concrete = "minecraft:light_gray_concrete"
		self.light_green_concrete = "minecraft:lime_concrete"

		self.redstone_block = "minecraft:redstone_block"
		self.redstone_dust = "minecraft:redstone"
		self.redstone_torch = "minecraft:redstone_torch"
		self.redstone_lamp = "minecraft:redstone_lamp"
		self.redstone_switch = "minecraft:lever"

		self.canvas = self.create_minecraft_canvas(self.render_distance, self.chunk_size)

	# Refactor according to minecraft coordinates: Current -> (16 x 12) * (16 x 12) * (16) & Layer one is light gray concrete
	def create_minecraft_canvas(self, render_distance, chunk_size):
		size = render_distance * chunk_size
		canvas = []

		for i in range(size):
			canvas.append([])
			for j in range(size):
				canvas[i].append([])
				for k in range(chunk_size):
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

	def generate_code(self):
		# Java edition: 1.13, 1.14, 1.15, 1.16, 1.17 and 1.18
		# /setblock <pos> <block> replace
		pass

	def show_canvas(self):
		print(self.canvas[:2])


if __name__ == '__main__':
	c = CodeGenerator()
	c.show_canvas()