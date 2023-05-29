// Specification
//
// Functionality: 
// if(A == B) then EQ = 1 else 0
// if(A > B) then GT = 1 else 0
// if(A < B) then LT = 1 else 0
//
// Input/s: A, B
// Output/s: EQ, GT, SM

module comparator(A, B, EQ, GT, SM);
	input [3:0] A,B;
	output EQ, GT, SM;

    assign EQ = (A == B);
    assign GT = (A > B);
    assign SM = (A < B);

endmodule