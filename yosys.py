import os
import re
import subprocess
import json
import glob
import platform


class Yosys:
	def __init__(self):
		# Select path based on operating system
		operating_system = platform.system()
		if operating_system == 'Linux':
			# sudo apt install yosys
			path = "/usr/bin/yosys"
		elif operating_system == 'Windows':
			path = "yosys\yosys.exe"

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
		# out, err = self.yosys.communicate(f"read_verilog {filepath}\n proc\n opt\n json -aig")
		out, err = self.yosys.communicate(
			f"read_verilog {filepath}\n json -aig")

		if (err != ""):
			return (1, err)

		# Remove newline and comments
		out = re.sub('\n', ' ', out)
		out = re.sub('/\* +\d+ +\*/', ' ', out)

		# Parse JSON string
		json_string = re.search('\{   "creator".*\}', out)
		netlist_json = None

		if json_string != None:
			netlist_json = json.loads(json_string.group(0))
		else:
			raise Exception(f"Failed to parse netlist")

		return (0, netlist_json)


if __name__ == '__main__':
	for verilog_file in glob.glob("test/*.v"):
		y = Yosys()
		netlist_json = y.process(filepath=verilog_file)

		with open(verilog_file.split('.')[0]+".json", 'w') as json_file:
			json.dump(netlist_json, json_file, indent=4)
