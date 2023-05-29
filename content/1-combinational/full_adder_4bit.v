// Specification
//
// Functionality: 
// S = Four bit binary addition of A & B
// COUT = Carry generated during addition if any
//
// Input/s: A, B, CIN
// Output/s: S, COUT

module full_adder_4bit(S, COUT, A, B, CIN); 
    input [3:0] A, B;
    input CIN;
    output [3:0] S;
    output COUT;

    assign {COUT, S} = A + B + CIN;    
endmodule