// Specification
//
// Functionality: 
// S = One bit binary addition of A & B
// C = Carry generated during addition if any
//
// Input/s: A, B
// Output/s: S, C

module half_adder(A, B, S, C);
	input A, B;
	output S, C;

	assign S = A ^ B;
	assign C = A & B;

endmodule