module shift_register(SO, SI, LR, clk, rst);
	input SI, LR, clk, rst;
	output SO;

	reg [4:0]SR;
  
  always@(posedge clk) begin
    if(!rst)
		SR <= 5'd0;
	
    if(LR)
      SR <= {SR[3:0], SI};
    else 
      SR <= {SI, SR[4:1]};
  end
  
  assign SO = LR? SR[4]: SR[0];
endmodule