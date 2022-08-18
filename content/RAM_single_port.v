module sram(q,data,addr,we,clk);
	input [7:0] data;
	input [5:0] addr;
	input we, clk;
	output [7:0] q;
	
	reg [7:0] sram[63:0];
	
	reg [5:0] addr_reg;
	
	always @ (posedge clk)
	begin
		if (we)
			ram[addr] <= data;
		addr_reg <= addr;
	end
		
	assign q = ram[addr_reg];
	
endmodule