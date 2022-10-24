import os
import re
import subprocess
import json
import glob
import platform


class Yosys:
    def __init__(self):
        operating_system = platform.system()
        if operating_system == 'Linux':
            # sudo apt install yosys
            path = "/usr/bin/yosys"

        if operating_system == 'Windows':
            raise Exception("Backend setup for Windows OS not supported!")

        self.yosys = subprocess.Popen(
            [path, '-Q', '-T'],
            shell=False,
            universal_newlines=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    def process(self, filepath):
        if not os.path.isfile(filepath):
            raise Exception(f"File not found: {filepath}")

        # Interact with yosys
        output, error = self.yosys.communicate(
            f"read_verilog {filepath} \nread_verilog - lib ./yosys/std.v \nsynth \ndfflibmap - liberty ./yosys/std.lib \nabc - liberty ./yosys/std.lib \nopt_clean \njson -aig")

        if (error != ""):
            return (1, error)

        # Remove newline and comments
        output = re.sub('\n', ' ', output)
        output = re.sub('/\* +\d+ +\*/', ' ', output)

        # Parse JSON string
        json_string = re.search('\{   "creator".*\}', output)
        netlist_json = None

        if json_string != None:
            netlist_json = json.loads(json_string.group(0))
        else:
            raise Exception(f"Failed to parse netlist")

        return (0, netlist_json)


if __name__ == '__main__':
    # verilog_file = "test/2x1_mux.v"
    # y = Yosys()
    # output = y.process(verilog_file)
    # print(output)

    for verilog_file in glob.glob("test/*.v"):
        y = Yosys()
        netlist_json = y.process(filepath=verilog_file)[1]

        with open(verilog_file.split('.')[0]+".json", 'w') as json_file:
            json.dump(netlist_json, json_file, indent=4)
