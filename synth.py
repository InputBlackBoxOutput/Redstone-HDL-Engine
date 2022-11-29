import glob
from yosys import Yosys
from router import router, plotter


class RedstoneSynth:
    def __init__(self):
        self.yosys = Yosys()
        self.netlist = None
        self.cell_layouts = {}
        self.module_layout = {}

    def load_file(self, filepath):
        success, output = self.yosys.process(filepath=filepath)

        if (success == 0):
            self.netlist_json = output
        else:
            raise Exception(f"Synth failed: {output}")

    def generate_module_layout(self):
        for m in self.netlist_json["modules"].keys():
            current_column = 0
            column_inputs = {0: []}

            layout = {'I': [], 'O': [], 0: []}
            module = self.netlist_json["modules"][m]

            for p in module["ports"]:
                port = module["ports"][p]

                if port["direction"] == "input":
                    layout['I'].append((p, port['bits']))

                if port["direction"] == "output":
                    layout['O'].append((p, port['bits']))

            for connection in layout['I']:
                column_inputs[0] += connection[1]

            for c in module["cells"]:
                cell = module["cells"][c]

                cell_input = []
                cell_output = []
                for connection in cell["connections"]:
                    if cell["port_directions"][connection] == "input":
                        cell_input.append(cell["connections"][connection][0])

                    if cell["port_directions"][connection] == "output":
                        cell_output.append(cell["connections"][connection][0])

                cell_info = (cell["type"], cell_input, cell_output)
                next_column_position = 0
                for i in range(0, current_column+1):
                    all_connections_present = True
                    for inpt in cell_input:

                        if inpt not in column_inputs[i]:
                            all_connections_present = False

                    if all_connections_present:
                        layout[i].append(cell_info)
                        next_column_position = i + 1
                        break
                else:
                    current_column += 1
                    layout[current_column] = []

                    layout[current_column].append(cell_info)
                    next_column_position = current_column + 1

                if next_column_position in column_inputs:
                    column_inputs[next_column_position] += cell_output
                else:
                    column_inputs[next_column_position] = list(cell_output)

            self.module_layout[m] = layout

    def generate_cell_layouts(self):
        for each_model in self.netlist_json["models"]:
            current_column = 0
            layout = {'I': [], 'O': [], 0: []}
            model = self.netlist_json["models"][each_model]

            for i, each_node in enumerate(model):
                if "port" in each_node[0]:
                    if each_node[0].startswith('n'):
                        layout['I'].append(
                            ('~', i, f"~{each_node[1]}{each_node[2]}"))
                    else:
                        layout['I'].append(
                            (' ', i, f"{each_node[1]}{each_node[2]}"))

                    if each_node[-2] == 'Y':
                        out = f"{each_node[-2]}{each_node[-1]}"
                        layout['O'].append((' ', i, out))

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
                            current_column -= 1

                    if each_node[0].startswith('n'):
                        layout[current_column].append(
                            ['~', [each_node[1], each_node[2]], out, "NAND"])
                    else:
                        layout[current_column].append(
                            [' ', [each_node[1], each_node[2]], out, "AND"])

                    current_column += 1
                    layout[current_column] = []

                if "true" in each_node[0]:
                    for n in range(len(each_node)):
                        if each_node[n] == 'Y':
                            layout['O'].append(
                                ('1', i, f"{each_node[1]}{each_node[n+1]}"))

                if "false" in each_node[0]:
                    for n in range(len(each_node)):
                        if each_node[n] == 'Y':
                            layout['O'].append(
                                ('0', i, f"{each_node[1]}{each_node[n+1]}"))

            remove = []
            for i in range(current_column+1):
                if layout[i] == []:
                    remove.append(i)

            for entity in remove:
                layout.pop(entity)

            self.cell_layouts[each_model] = layout

    def synthesize(self):
        return str(self.dump_json())


if __name__ == "__main__":
    verilog_file = "test/mux.v"

    s = RedstoneSynth()
    s.load_file(verilog_file)

    print("\nCell layout/s:\n")
    s.generate_cell_layouts()
    for model in s.cell_layouts:
        print(model)
        for cols in s.cell_layouts[model]:
            print(cols, s.cell_layouts[model][cols])

    print("\nModule layout:\n")
    s.generate_module_layout()
    for module in s.module_layout:
        print(module)
        for col in s.module_layout[module]:
            print(col, s.module_layout[module][col])

    # for verilog_file in glob.glob("test/*.v"):
    #     print(f"\nFile: {verilog_file}")
    #     s = RedstoneSynth()
    #     s.load_file(verilog_file)

    #     print("\nCell layout/s:\n")
    #     s.generate_cell_layouts()
    #     for model in s.cell_layouts:
    #         print(model)
    #         for cols in s.cell_layouts[model]:
    #             print(cols, s.cell_layouts[model][cols])

    #     print("\nModule layout:\n")
    #     s.generate_module_layout()
    #     for module in s.module_layout:
    #         print(module)
    #         for col in s.module_layout[module]:
    #             print(col, s.module_layout[module][col])

    #     print("\n" + '-' * 70)
