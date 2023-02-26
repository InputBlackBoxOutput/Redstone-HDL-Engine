// Specification
//
// Functionality: 
// Detect a sequence using a FSM
//
// Input/s: IN, RST, CLK
// Output/s: DET

module sequence_detector(IN, DET, RST, CLK);
	input IN;
	output reg DET;

	input RST;
	input CLK;

	reg [2:0] PR_STAGE, NX_STAGE; 
	parameter s0 = 3'b000;
	parameter s1 = 3'b010;
	parameter s2 = 3'b011;
	parameter s3 = 3'b100;
	
	always@(posedge CLK) begin
		if(RST)
			PR_STAGE <= s0;
		else
			PR_STAGE <= NX_STAGE; 
	end

	always@(PR_STAGE, IN)
	case(PR_STAGE)

		// State 0
		s0:if(IN == 1)
			NX_STAGE = s1;
		else
			NX_STAGE = s0;

		// State 1
		s1:if(IN == 0)
			NX_STAGE = s2;
		else
			NX_STAGE = s1;

		// State 2
		s2:if(IN == 1)
			NX_STAGE=s3;
		else
			NX_STAGE=s0;

		// State 3
		s3:if(IN == 1)
			NX_STAGE=s1;
		else
			NX_STAGE=s2;
		
		default:NX_STAGE=s0;
	endcase


	always@(PR_STAGE)
	case(PR_STAGE)
		s0: DET=0;
		s1: DET=0;
		s2: DET=0;
		s3: DET=1;
		default: DET=0;
	endcase
endmodule