// Specification
//
// Functionality: 
// S = One bit binary addition of A & B
// COUT = Carry generated during addition if any
//
// Input/s: A, B, CIN
// Output/s: S, COUT

module full_adder_1bit(S, COUT, A, B, CIN); 
	input A, B, CIN;
	output S, COUT;

	assign S = (A ^ B) ^ CIN;
	assign COUT=(A & B)|(A & CIN)|(B & CIN);
endmodule