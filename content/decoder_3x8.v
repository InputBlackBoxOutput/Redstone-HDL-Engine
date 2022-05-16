module decoder_3x8(Y, I, En);

    input [2:0]I;
    input En;
    output [7:0]Y;

    assign Y = {En & ~I[0] & ~I[1] & ~I[2],
                En & ~I[0] & ~I[1] & I[2],
                En & ~I[0] & I[1] & ~I[2],
                En & ~I[0] & I[1] & I[2],
                En & I[0] & ~I[1] & ~I[2],
                En & I[0] & ~I[1] & I[2],
                En & I[0] & I[1] & ~I[2],
                En & I[0] & I[1] & I[2]};

endmodule