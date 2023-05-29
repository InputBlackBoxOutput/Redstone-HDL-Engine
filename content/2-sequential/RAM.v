// Specification
//
// Functionality: 
// Write to memory
// if(WE == 1) then MEM[ADDR] = DATA
// Read from memory
// if(WE == 0) then Q = MEM[ADDR]
//
// Input/s: DATA, ADDR, WE, CLK
// Output/s: Q

module RAM(Q, DATA, ADDR, WE, CLK);
	input [7:0] DATA;
	input [5:0] ADDR;
	input WE, CLK;
	output [7:0] Q;
	
	reg [7:0] memory[63:0];
	reg [5:0] ADDR_REG;
	
	always @ (posedge CLK)
	begin
		if (WE)
			memory[ADDR] <= DATA;
		
		ADDR_REG <= ADDR;
	end
		
	assign Q = memory[ADDR_REG];
	
endmodule