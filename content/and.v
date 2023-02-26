// Specification
//
// Functionality: 
// Y = A & B
//
// Input/s: A, B
// Output/s: Y

module _and(Y, X1, X2);
  input X1, X2;
  output Y;
  
  assign Y = X1 & X2;
endmodule