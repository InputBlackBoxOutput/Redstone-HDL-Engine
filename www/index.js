const verilog_code = document.getElementById("verilog-code");

verilog_code.value = `module m(a,b);\ninput a;\noutput b;\nwire a = ~b;\nendmodule`;
