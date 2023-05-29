// Specification
//
// Functionality: 
// Y = X1 & X2
//
// Input/s: X1, X2
// Output/s: Y

module _and(Y, X1, X2);
  input X1, X2;
  output Y;
  
  assign Y = X1 & X2;
endmodule