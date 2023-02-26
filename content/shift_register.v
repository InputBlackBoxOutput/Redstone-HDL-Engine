// Specification
//
// Functionality: 
// Serial In Serial Out shift register
//
// Input/s: SI, LR, CLK, RST
// Output/s: SO

module shift_register(SI, LR, CLK, RST, SO);
	input SI, LR, CLK, RST;
	output SO;

	reg [4:0] SR;
  
  always@(posedge CLK) begin
    if(!RST)
		SR <= 5'd0;
	
    if(LR)
      SR <= {SR[3:0], SI};
    else 
      SR <= {SI, SR[4:1]};
  end
  
  assign SO = LR? SR[4]: SR[0];
endmodule