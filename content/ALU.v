// Specification
//
// Functionality: 
// OPCODE == 00 => X1 + X2
// OPCODE == 01 => X1 - X2
// OPCODE == 10 => X1 & X2
// OPCODE == 11 => ~X1
//
// Input/s: A, B, OPCODE, CLK
// Output/s: Y

module ALU(A, B, Y, OPCODE, CLK);
    input [7:0]A, B;
    input [1:0]OPCODE;
    input CLK;
    output [7:0]Y;

    always@(posedge CLK) begin
        case(OPCODE)
            1'b00: Y = A + B;
            1'b01: Y = A - B;
            1'b10: Y = A & B;
            1'b11: Y = ~A;
        endcase
    end

endmodule