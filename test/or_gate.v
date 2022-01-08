module or_gate(X, Y);
    input [0:1]X;
    output Y;
    wire Y;

    assign Y = X[0] | X[1];
endmodule