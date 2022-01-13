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


var img = new Image();
img.src = "images/dummy-diagram.png";

function zoom() {
    const canvas_div = document.getElementById('diagram-canvas-div');
    const canvas = document.getElementById('diagram-canvas');
    canvas.width = canvas_div.clientWidth;
    canvas.height = canvas_div.clientHeight;

    var ctx = canvas.getContext('2d');
    var control = new CanvasManipulation(
        canvas
        , function () {draw(ctx)}
    )
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

window.onload = zoom;