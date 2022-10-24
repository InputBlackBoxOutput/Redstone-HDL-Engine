module adder(A, B, S, C);
    input A;
    input B;
    output S;
    output C;

    assign S = A ^ B;
    assign C = A & B;

endmodule