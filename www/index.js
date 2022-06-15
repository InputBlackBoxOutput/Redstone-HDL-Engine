const verilog_code = document.getElementById("verilog-code");
const synthesize_btn = document.getElementById("synthesize");
const diagram = document.getElementById("diagram-div");

const BACKEND_ENDPOINT = "https://redstone-hdl.herokuapp.com";

// Setup CodeMirror
verilog_code.value =
  "module m(a,b);\n\tinput a;\n\toutput b;\n\n\twire a = ~b;\nendmodule";

code_editor = CodeMirror.fromTextArea(verilog_code, {
  lineNumbers: true,
  tabSize: 2,
  mode: "verilog",
  theme: "monokai",
});


// Diagram
function generateDiagram() {
  var data = "module m(a,b); input a; output b; wire a = ~b; endmodule";

  axios.post('https://redstone-hdl.herokuapp.com/netlist', data,
    {
      headers: {
        'Content-Type': 'text/plain'
      }
    })
    .then(async function (response) {
      let diagram_svg = await netlistsvg.render(netlistsvg.digitalSkin, { "modules": response.data.output.modules });
      diagram.innerHTML = diagram_svg;
    })
    .catch(function (error) {
      console.log(error);
      alert("Something went wrong while generating diagram!");
    });
}

// Setup synthesize button
synthesize_btn.addEventListener('click', () => {
  generateDiagram();
})

window.onload = () => {
  // Resize code textarea
  col_height = document.getElementById("verilog-code-div").clientHeight - 95;
  code_editor.setSize(null, col_height);

  // Connect with backend
  synthesize_btn.disabled = true;

  axios.get(`${BACKEND_ENDPOINT}`)
    .then(() => {
      synthesize_btn.disabled = false
    })
    .catch((error) => {
      console.log(error);
      alert("Unable to connect to backend!");
    })
};