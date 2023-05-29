// Specification
//
// Functionality: 
// Y = X[0] & X[1] & X[2] & X[3]
//
// Input/s: X
// Output/s: Y

module reduce_and(X, Y);
    input [3:0] X;
    output Y;

    assign Y = &X;
endmodule