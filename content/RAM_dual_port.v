// Specification
//
// Functionality: 
// Write to memory
// if(WE_X == 1) then MEM[ADDR_X] = DATA_X
// Read from memory
// if(WE_X == 0) then Q_X = MEM[ADDR_X]
//
// Input/s: DATA_A, DATA_B, ADDR_A, ADDR_B, WE_A, WE_B, CLK
// Output/s: Q_A, Q_B

module RAM(Q_A, Q_B, DATA_A, DATA_B, ADDR_A, ADDR_B, WE_A, WE_B, CLK);
	input [7:0] DATA_A, DATA_B;
	input [5:0] ADDR_A, ADDR_B;
	input WE_A, WE_B, CLK;
	output reg [7:0] Q_A, Q_B;

	reg [7:0] memory [63:0];
	
	// Port A
	always @ (posedge CLK)
	begin
		if (WE_A) 
		begin
			memory[ADDR_A] <= DATA_A;
			Q_A <= DATA_A;
		end
		else 
		begin
			Q_A <= memory[ADDR_A];
		end
	end
	
	// Port B
	always @ (posedge CLK)
	begin
		if (WE_B)
		begin
			memory[ADDR_B] <= DATA_B;
			Q_B <= DATA_B;
		end
		else
		begin
			Q_B <= memory[ADDR_B];
		end
	end
	
endmodule
