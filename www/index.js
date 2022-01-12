const verilog_code = document.getElementById('verilog-code')
verilog_code.value = "module m(a,b);\n\tinput a;\n\toutput b;\n\n\twire a = ~b;\nendmodule"

code = CodeMirror.fromTextArea(verilog_code, {
    lineNumbers: true,
    tabSize: 2,
    mode: 'verilog',
    theme: 'monokai'
    });
code.setSize(null, 620);


const synthesize_btn = document.getElementById("synthesize");
synthesize_btn.disabled = true;