module reduce_and(X, Y);
    input [3:0] X;
    output Y;

    assign Y = &X;
endmodule