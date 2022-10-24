module mux(D, S, Y);
    input [1:0]D;
    input S;
    output Y;

    assign Y = S? D[1] : D[0];
endmodule