// Specification
//
// Functionality: 
// FREQ(CLK_OUT) = FREQ(CLK) / 2 
// 
//
// Input/s: CLK, RST
// Output/s: CLK_OUT

module frequency_divider( CLK, RST, CLK_OUT );
	output reg CLK_OUT;
	input CLK ;
	input RST;

	always @(posedge CLK) begin
		if (~RST)
			CLK_OUT <= 1'b0;
		else
			CLK_OUT <= ~CLK_OUT;	
		end
endmodule