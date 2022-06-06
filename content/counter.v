module up_down_counter(UD, Q, clk, rst);
  input UD, clk, rst;
  output [7:0]Q;
  
  reg [7:0]counter_reg;
  
  always@(negedge clk) begin
    if(!rst)
  		counter_reg <= 8'b0;
    
    if(UD)
      counter_reg <= counter_reg + 1;
    else
      counter_reg <= counter_reg - 1;
    
  end
  
  assign Q = counter_reg;
endmodule