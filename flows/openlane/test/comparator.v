module comparator (A, B, G, E, L);
    input [1:0]A, B;
    output reg G, E, L;

    always@(A or B)
    begin
        L <= A < B;
        G <= A > B;
        E <= A == B;
    end
endmodule