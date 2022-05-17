module barrel_shifter(out, in, lr, n);

	input [7:0]In;
	input [2:0]n;
	input lr;
	output reg [7:0]out;

	always@(*) begin
		if(lr)
			out = in << n;
		else
			out = in >> n;
	end

endmodule