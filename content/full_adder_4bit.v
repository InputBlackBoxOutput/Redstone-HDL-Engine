module full_adder_4bit(s, cout, a, b, cin); 
    input [3:0] a, b;
    input cin;
    output [3:0] s;
    output cout;

    assign {cout,s} = a + b + cin;
    
endmodule