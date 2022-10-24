import glob
from yosys import Yosys 
from router import router, plotter

class RedstoneSynth:
	def __init__(self):
		self.yosys = Yosys()
		self.netlist_json = None
		
		self.model_aig = {}
		self.ports = []
		self.cells = []
		self.net = []

	def load_file(self, filepath):
		success, self.netlist_json = self.yosys.process(filepath=filepath)
		
		if(success):
			self.__extractModelAIG()
			self.__extractNetlist()

	def __extractModelAIG(self):
		for each_model in self.netlist_json["models"]:
			model = self.netlist_json["models"][each_model]
			
			node_map = {}
			graph = []
			and_index = 0

			for i, each_node in enumerate(model):
				if "port" in each_node[0]:
					if each_node[0].startswith('n'):
						node_map[i] = f"~{each_node[1]}{each_node[2]}"
					else:
						node_map[i] = f"~{each_node[1]}{each_node[2]}"

				if "and" in each_node[0]:
					if each_node[-2] == 'Y':
						graph.append((i, f"{each_node[-2]}{each_node[-1]}"))
						
					graph.append((each_node[1], i))
					graph.append((each_node[2], i))
					
					if each_node[0].startswith('n'):
						node_map[i] = f"NAND {and_index}"
					else:
						node_map[i] = f"AND {and_index}"

					and_index += 1
						
		 
				if "true" in each_node[0]:
					for n in range(len(each_node)):
						if each_node[n] == 'Y':
							graph.append(("L1", f"Y{n}"))
							node_map[i] = "L1"

				
				if "false" in each_node[0]:
					for n in range(len(each_node)):
						if each_node[n] == 'Y':
							graph.append(("L0", f"Y{n}"))
							node_map[i] = "L0"

			mapped_graph = []
			for edge in graph:
				if 'Y' not in str(edge[0]) and 'L' not in str(edge[0]):
					src = node_map[edge[0]]
				else:
					src = edge[0]

				if 'Y' not in str(edge[1]) and 'L' not in str(edge[0]):
					dst = node_map[edge[1]]
				else:
					dst = edge[1]
				
				mapped_graph.append((src, dst))

			self.model_aig[each_model] = mapped_graph
	
	def __extractNetlist(self):
		for module in self.netlist_json["modules"].keys():
			m = self.netlist_json["modules"][module]
			
			for port in m["ports"]:
				p = m["ports"][port]
				self.ports.append((port, p["direction"], p["bits"]))

			for cell in m["cells"]:
				c = m["cells"][cell]
				try:
					model = c["model"]
					self.cells.append((c["type"], model, c["parameters"], c["port_directions"], c["connections"]))
				except:
					self.cells.append((c["type"], c["parameters"], c["port_directions"], c["connections"]))

			for net in m["netnames"]:
				n = m["netnames"][net]
				self.net.append((net, n["bits"]))

	def dump_model_aig(self):
		print("Model AIG:")
		for each_model in self.model_aig:
			print(each_model)
			for entity in self.model_aig[each_model]:
				print(entity)

	def dump_ports(self):
		print("\nPorts:")
		for each in s.ports:
			print(each)

	def dump_cells(self):
		print("\nCells:")
		for each in s.cells:
			print(each)

	def dump_net(self):
		print("\nNet:")
		for each in s.net:
			print(each)
			
	def dump(self):
		self.dump_model_aig()
		self.dump_ports()
		self.dump_cells()
		self.dump_net()

	def dump_json(self):
		json_data = {}
		json_data["model_aig"] = self.model_aig
		json_data["ports"] = self.ports
		json_data["cells"] = self.cells
		json_data["net"] = self.net

		return json_data

	def generate_cell_layouts(self):
		self.cell_layouts = {}

		for each_model in self.netlist_json["models"]:
			current_col = 0
			layout = {'I':[], 'O':[], 0:[]}
			model = self.netlist_json["models"][each_model]

			for i, each_node in enumerate(model):
				if "port" in each_node[0]:
					if each_node[0].startswith('n'):
						layout['I'].append(('~', i, f"~{each_node[1]}{each_node[2]}"))
					else:
						layout['I'].append((' ', i, f"{each_node[1]}{each_node[2]}"))

				if "and" in each_node[0]:
					out = i
					if each_node[-2] == 'Y':
						out = f"{each_node[-2]}{each_node[-1]}"
						layout['O'].append((' ', i, out))

					# Subsequent independent AND/NAND gates
					if 'and' in model[i-1][0] and 'and' in model[i][0]:
						inpts = model[i][1:]
						prev_out = i-1

						if prev_out not in inpts:
							current_col -= 1

					if each_node[0].startswith('n'):
						layout[current_col].append(['~', [each_node[1], each_node[2]], out, "NAND"])
					else:
						layout[current_col].append([' ', [each_node[1], each_node[2]], out, "AND"])
						
					current_col += 1
					layout[current_col] = []

				if "true" in each_node[0]:
					for n in range(len(each_node)):
						if each_node[n] == 'Y':
							layout['O'].append(('1', i, f"{each_node[1]}{each_node[n+1]}"))
				
				if "false" in each_node[0]:
					for n in range(len(each_node)):
						if each_node[n] == 'Y':
							layout['O'].append(('0', i, f"{each_node[1]}{each_node[n+1]}"))

			remove = []
			for i in range(current_col+1):
				if layout[i] == []:
					remove.append(i)

			for entity in remove:
				layout.pop(entity) 

			self.cell_layouts[each_model] = layout

	def synthesize(self):
		return str(self.dump_json())

if __name__ == "__main__":
	for verilog_file in glob.glob("test/*.v"):
		print(f"\nFile: {verilog_file}")
		s = RedstoneSynth(verilog_file)
		s.dump()
		

		print("\nCell layout/s:\n")
		s.generate_cell_layouts() 
		for i in s.cell_layouts:
			print(i)
			for j in s.cell_layouts[i]:
				print(j, s.cell_layouts[i][j])

		print("\n" + '-' * 70)

	# A = ['0', 'A', 'D', 'E', 'A', 'F', 'G', '0', 'D', 'I', 'J', 'J']
	# B = ['B', 'C', 'E', 'C', 'E', 'B', 'F', 'H', 'I', 'H', 'G', 'I']

	# r = router.Router(A, B)
	# output = r.route()

	# print("\nRouter output:")
	# print(output)

	# p = plotter.Plotter()
	# p.draw(output[0], output[1], output[2])
	# p.show()
