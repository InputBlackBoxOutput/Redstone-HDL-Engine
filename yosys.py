import os, platform, subprocess
import re, json, secrets

class Yosys:
    def __init__(self):
        if platform.system() == 'Linux':
            path = "/usr/bin/yosys"

            if not os.path.exists(path):
                print("Yosys not installed")

            self.yosys = subprocess.Popen(
                [path, '-Q', '-T'],
                shell=False,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

    def generate_netlist_json(self, filepath):
        if not os.path.isfile(filepath):
            raise Exception(f"File not found: {filepath}")

        output, error = self.yosys.communicate(f"read_verilog {filepath} \nread_verilog - lib ./yosys/std.v \nsynth \ndfflibmap - liberty ./yosys/std.lib \nabc - liberty ./yosys/std.lib \nopt_clean \njson -aig")
        
        if error == "":
            output = re.sub('\n', ' ', output)
            output = re.sub('/\* +\d+ +\*/', ' ', output)
            json_string = re.search('\{   "creator".*\}', output)

            if json_string != None:
                netlist_json = json.loads(json_string.group(0))
            else:
                raise Exception("Something went wrong while parsing netlist")
        else:
            raise Exception("Something went wrong while generating netlist")

        return netlist_json

    def extract_module_layout(self, netlist_json):
        module_layout = {}

        for m in netlist_json["modules"].keys():
            current_column = 0
            column_inputs = {0: []}

            layout = {'I': [], 'O': [], 0: []}
            module = netlist_json["modules"][m]

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

                module_layout[m] = layout

        return module_layout

    def generate_diagram_json(self, filepath):
        netlist_json = self.generate_netlist_json(filepath=filepath)
        module_layout = self.extract_module_layout(netlist_json)
        module = list(module_layout.keys())[0]

        # Generate nodes for the netlist and collect connections between nodes
        nodes = []
        connections = {}
        for key in module_layout[module].keys():
            for cell in module_layout[module][key]:
                if key == "I":
                    nodes.append(
                        {
                            "id": cell[0],
                            "width": 40,
                            "height": 40,
                            "type": "INPUT"
                        }
                    )

                    for pin in cell[1]:
                        connections[pin] = ["O-" + cell[0]]

                if key == "O":
                    nodes.append(
                        {
                            "id": cell[0],
                            "width": 80,
                            "height": 80,
                            "type": "OUTPUT"
                        }
                    )

                    for pin in cell[1]:
                        connections[pin] = ["I-" + cell[0]]

                if key != "I" and key != "O":
                    cell_id = f"{cell[0][2:-1]}-{secrets.token_hex(nbytes=2)}"

                    nodes.append(
                        {
                            "id": cell_id,
                            "width": 80,
                            "height": 80,
                            "type": f"{cell[0][2:-1]}"
                        }
                    )

                    for pin in cell[1]:
                        try:
                            connections[pin].append("I-" + cell_id)
                        except KeyError:
                            connections[pin] = ["I-" + cell_id]

                    for pin in cell[2]:
                        try:
                            connections[pin].append("O-" + cell_id)
                        except KeyError:
                            connections[pin] = ["O-" + cell_id]

        # Process connections to create edges for the netlist
        for connection in connections:
            connections[connection].sort(reverse=True)

        edges = []
        target_handle_tracker = {}
        for connection in connections:
            for i in range(len(connections[connection]) - 1):
                try:
                    target_handle_tracker[connections[connection][i + 1]] += 1
                except:
                    target_handle_tracker[connections[connection][i + 1]] = 1

                if "-" in connections[connection][i + 1][2:]:
                    target_handle = f"X{target_handle_tracker[connections[connection][i + 1]]}"
                else:
                    target_handle = ""

                edges.append(
                    { 
                        "id": secrets.token_hex(nbytes=2), 
                        "sources": [connections[connection][0][2:]], 
                        "targets": [connections[connection][i + 1][2:]],
                        "targetHandle": target_handle
                    }
                )

        edges.reverse()
        return {"nodes": nodes, "edges": edges}
       

        
if __name__ == '__main__':
    y = Yosys()
    diagram_json = y.generate_diagram_json(filepath="test/yosys/0-elementary/and_gate.v")
    # diagram_json = y.generate_diagram_json(filepath="test/yosys/1-combinational/comparator.v")

    import json
    with open("output.json", 'w') as json_file:
        json.dump(diagram_json, json_file)
