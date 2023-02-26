// Specification
//
// Functionality: 
// First In First Out buffer for streaming IO
//
// Input/s: CLK, RST, BUFFER_IN, WR_EN, RD_EN
// Output/s: BUFFER_OUT, EMPTY, FULL, COUNT

module FIFO(CLK, RST, BUFFER_IN, BUFFER_OUT, WR_EN, RD_EN, EMPTY, FULL, COUNT);
   input RST, CLK, WR_EN, RD_EN;   
   input [7:0] BUFFER_IN;
   output reg [7:0] BUFFER_OUT;                       
   output reg [3:0] COUNT;
   output reg EMPTY, FULL;  

   reg[2:0] rd_ptr, wr_ptr;           
   reg[7:0] buf_mem[7:0];   

   always @(COUNT)
   begin
      EMPTY = (COUNT==0);
      FULL = (COUNT== 8);

   end

   always @(posedge CLK or posedge RST)
   begin
      if( RST )
         COUNT <= 0;

      else if( (!FULL && WR_EN) && ( !EMPTY && RD_EN ) )
         COUNT <= COUNT;

      else if( !FULL && WR_EN )
         COUNT <= COUNT + 1;

      else if( !EMPTY && RD_EN )
         COUNT <= COUNT - 1;
      else
         COUNT <= COUNT;
   end

   always @( posedge CLK or posedge RST)
   begin
      if( RST )
         BUFFER_OUT <= 0;
      else
      begin
         if( RD_EN && !EMPTY )
            BUFFER_OUT <= buf_mem[rd_ptr];

         else
            BUFFER_OUT <= BUFFER_OUT;

      end
   end

   always @(posedge CLK)
   begin

      if( WR_EN && !FULL )
         buf_mem[ wr_ptr ] <= BUFFER_IN;

      else
         buf_mem[ wr_ptr ] <= buf_mem[ wr_ptr ];
   end

   always@(posedge CLK or posedge RST)
   begin
      if( RST )
      begin
         wr_ptr <= 0;
         rd_ptr <= 0;
      end
      else
      begin
         if( !FULL && WR_EN )    wr_ptr <= wr_ptr + 1;
            else  wr_ptr <= wr_ptr;

         if( !EMPTY && RD_EN )   rd_ptr <= rd_ptr + 1;
         else rd_ptr <= rd_ptr;
      end

   end
endmodule

