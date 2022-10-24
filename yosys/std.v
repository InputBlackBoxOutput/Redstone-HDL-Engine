// Cell library helper verilog for yosys

module BUF(A, Y);
    input A;
    output Y;
    assign Y = A;
endmodule

module NOT(A, Y);
    input A;
    output Y;
    assign Y = ~A;
endmodule

module NOR(A, B, Y);
    input A, B;
    output Y;
    assign Y = ~(A | B);
endmodule

module NAND(A, B, Y);
    input A, B;
    output Y;
    assign Y = ~(A & B);
endmodule

module DFF(C, D, Q);
    input C, D;
    output reg Q;
    always @(posedge C)
        Q <= D;
endmodule