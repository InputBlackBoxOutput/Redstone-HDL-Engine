const verilog_code = document.getElementById('verilog-code')
verilog_code.value = "module m(a,b);\ninput a;\noutput b;\nwire a = ~b;\nendmodule"

code = CodeMirror.fromTextArea(verilog_code, {
    lineNumbers: true,
    tabSize: 2,
    mode: 'verilog',
    theme: 'monokai'
    });
code.setSize(null, 605);