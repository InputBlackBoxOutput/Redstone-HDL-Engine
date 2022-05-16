module comparator_4bit(eq, gt, sm, A, B);

	input [3:0] A,B;
	output eq, gt, sm;

    assign eq = (A == B);
    assign gt = (A > B);
    assign sm = (A < B);

endmodule