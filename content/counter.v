// Specification
//
// Functionality: 
// if(UD == 1) then count += 1 
// if(UD == 0) then count -= 1
//
// Input/s: UD, CLK, RST 
// Output/s: Q

module counter(UD, Q, CLK, RST);
  input UD, CLK, RST;
  output [7:0]Q;

  reg [7:0] COUNT;
  
  always@(posedge CLK) begin
    if(!RST)
  		COUNT <= 8'b0;

    if(UD)
      COUNT <= COUNT + 1;
    else
      COUNT <= COUNT - 1;
  end
  
  assign Q = COUNT;
endmodule