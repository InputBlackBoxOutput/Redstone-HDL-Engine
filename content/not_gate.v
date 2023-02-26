// Specification
//
// Functionality: 
// Y = !X
//
// Input/s: X
// Output/s: Y

module _not(Y, X);
  input X;
  output Y;
  
  assign Y = ~X;
endmodule