import glob
from yosys import Yosys 
from router import router, plotter

class RedstoneSynth:
    def __init__(self, filepath, path="yosys/yosys.exe"):
        self.yosys = Yosys(path)
        self.netlist_json = self.yosys.process(filepath=filepath)
        
        self.model_aig = []
        self.ports = []
        self.cells = []
        self.net = []

        self.__extractModelAIG()
        self.__extractNetlist()
            
    def __extractModelAIG(self):
        for each_model in self.netlist_json["models"]:
            ports = []
            and_gates = []
            true = []
            false = []

            for i, each_node in enumerate(self.netlist_json["models"][each_model]):
                if "port" in each_node[0]:
                    _not = '~' if each_node[0].startswith('n') else ''
                    each_node.pop(0)
                    ports.append((i, _not, *each_node))

                if "and" in each_node[0]:
                    _not = '~' if each_node[0].startswith('n') else ''
                    each_node.pop(0)

                    if len(each_node) > 4:
                        each_node.pop(4)
                        each_node.pop(4)

                    and_gates.append((i, _not, *each_node))
                
                if "true" == each_node[0]:
                    each_node.pop(0)
                    true.append(each_node)

                if "false" == each_node[0]:
                    each_node.pop(0)
                    false.append(each_node)

            self.model_aig.append((each_model, ports, and_gates, true, false))
    
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
        for model in self.model_aig:
            print(model[0])
            for node in model[1]:
                print(node)

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

    def synthesize(self):
        return self.dump_json()

if __name__ == "__main__":
    for verilog_file in glob.glob("test\*.v"):
        print(f"\nFile: {verilog_file}")
        s = RedstoneSynth(verilog_file)
        s.dump()


    A = ['0', 'A', 'D', 'E', 'A', 'F', 'G', '0', 'D', 'I', 'J', 'J']
    B = ['B', 'C', 'E', 'C', 'E', 'B', 'F', 'H', 'I', 'H', 'G', 'I']

    r = router.Router(A, B)
    output = r.route()

    print("\nRouter output:")
    print(output)

    p = plotter.Plotter()
    p.draw(output[0], output[1], output[2])
    p.show()
