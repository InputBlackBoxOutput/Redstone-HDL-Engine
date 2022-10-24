module _or(X, Y);
    input [0:1]X;
    output Y;

    assign Y = X[0] | X[1];
endmodule