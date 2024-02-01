module counter(C, CLK, RST);
    input CLK, RST;
    output reg [7:0]C;

    always@(posedge CLK) begin
        if(RST)
            C = 0;
        else
            C = C + 1;
    end
endmodule