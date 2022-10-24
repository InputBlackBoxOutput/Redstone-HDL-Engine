# https://github.com/YosysHQ/yosys/tree/master/examples/cmos

CONTRAPTION=test
LIB_VERILOG=std.v
LIB=std.lib
TIME = $$(date +'%Y%m%d-%H%M%S')

synth: clean
	echo "read_verilog ${CONTRAPTION}.v" > synth.ys
	echo "read_verilog -lib $(LIB_VERILOG)" >> synth.ys
	echo "synth" >> synth.ys
	echo "dfflibmap -liberty $(LIB)" >> synth.ys
	echo "abc -liberty $(LIB)" >> synth.ys
	echo "opt_clean" >> synth.ys
	echo "stat -liberty ${LIB}" >> synth.ys
	echo "write_json synth.json" >> synth.ys
	echo "show -colors $(TIME)" >> synth.ys
	yosys synth.ys

clean:
	rm -rf synth.ys synth.json
