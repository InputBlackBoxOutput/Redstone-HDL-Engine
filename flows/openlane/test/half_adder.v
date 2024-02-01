module half_adder(A, B, S, C);
	input A, B;
	output S, C;

	assign S = A ^ B;
	assign C = A & B;

endmodule