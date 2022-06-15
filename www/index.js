const verilog_code = document.getElementById("verilog-code");
const canvas_div = document.getElementById("diagram-canvas-div");
const canvas = document.getElementById("diagram-canvas");
const synthesize_btn = document.getElementById("synthesize");

// Preload image
var img = new Image();
img.src = "images/dummy-diagram.png";

// Setup CodeMirror
verilog_code.value =
  "module m(a,b);\n\tinput a;\n\toutput b;\n\n\twire a = ~b;\nendmodule";

code = CodeMirror.fromTextArea(verilog_code, {
  lineNumbers: true,
  tabSize: 2,
  mode: "verilog",
  theme: "monokai",
});

// Setup diagram zoom
function zoom() {
  canvas.hidden = false;
  canvas.width = canvas_div.clientWidth;
  canvas.height = canvas_div.clientHeight;

  var ctx = canvas.getContext("2d");
  var control = new CanvasManipulation(
    canvas,
    function () {
      draw(ctx);
    },
    { leftTop: { x: 0, y: 0 }, rightBottom: { x: 10000, y: 10000 } }
  );
  control.init();
  control.layout();
  draw(ctx);
}

function draw(ctx) {
  ctx.clearCanvas();
  ctx.drawImage(img, 0, 0);

  // Display text on canvas
  // ctx.beginPath()
  // ctx.fillStyle = '#000'
  // ctx.font = 'bold 80px Arial'
  // ctx.fillText('Hello, world!', 50, 100)
  // ctx.closePath()
}

window.onload = () => {
  // Enable diagram zoom
  zoom();

  // Resize code textarea
  col_height = document.getElementById("verilog-code-div").clientHeight - 95;
  console.log(col_height);
  code.setSize(null, col_height);

  // Disable synthesize button
  synthesize_btn.disabled = true;
};
