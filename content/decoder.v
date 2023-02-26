// Specification
//
// Functionality: 
// Binary representation to one hot representation
//
// Input/s: I, EN
// Output/s: Y

module decoder(Y, I, EN);
    input [2:0]I;
    input EN;
    output [7:0]Y;

    assign Y = {
        EN & ~I[0] & ~I[1] & ~I[2],
        EN & ~I[0] & ~I[1] &  I[2],
        EN & ~I[0] &  I[1] & ~I[2],
        EN & ~I[0] &  I[1] &  I[2],
        EN &  I[0] & ~I[1] & ~I[2],
        EN &  I[0] & ~I[1] &  I[2],
        EN &  I[0] &  I[1] & ~I[2],
        EN &  I[0] &  I[1] &  I[2]
    };
endmodule