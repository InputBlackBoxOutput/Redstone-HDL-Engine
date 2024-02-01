module _and(X, Y);
    input [1:0]X;
    output Y;

    assign Y = X[0] & X[1];
endmodule