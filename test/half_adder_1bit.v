module half_adder_1bit(a,b,s,c);
	input a,b;
	output s,c;

	assign s = a ^ b;
	assign c = a & b;

endmodule