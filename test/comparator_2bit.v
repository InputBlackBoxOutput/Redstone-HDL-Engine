module comparator (A0, A1, B0, B1, G, E, L);
    input A0, A1, B0, B1;
    output G, E, L;
    reg G, E, L;

    always@(A0 or A1 or B0 or B1)
    begin
        L <= {A1, A0} < {B1, B0};
        G <= {A1, A0} > {B1, B0};
        E <= {A1, A0} == {B1, B0};
    end
endmodule