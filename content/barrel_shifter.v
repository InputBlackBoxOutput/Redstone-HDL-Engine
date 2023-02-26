// Specification
//
// Functionality: 
// LR == 1 => OUT = LSHF(IN, N)
// LR == 0 => OUT = RSHF(IN, N)
//
// Input/s: IN, LR, N
// Output/s: OUT

module barrel_shifter(OUT, IN, LR, N);
	input [7:0]IN;
	input [2:0]N;
	input LR;
	output reg [7:0]OUT;

	always@(*) begin
		if(LR)
			OUT = IN << N;
		else
			OUT = IN >> N;
	end

endmodule