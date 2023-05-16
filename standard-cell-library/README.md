# Standard Cell Library

Derivative of [High Voltage Sky130 Factory Standard Cell Library](https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hvl/tree/4fd4f858d16c558a6a488b200649e909bb4dd800
)

|# | Cell type | Cell | Description | Mapped to Redstone |
|--|--|--|--|--|
|1 | Combinational | inv | Inverter ||
|2 | Combinational | nand2 | 2-input NAND ||
|3 | Combinational | nand3 | 3-input NAND ||
|4 | Combinational | nor2 | 2-input NOR ||
|5 | Combinational | nor3 | 3-input NOR ||
|6 | Combinational | a22oi | 2-input AND into both inputs of 2-input NOR ||
|7 | Combinational | a21oi | 2-input AND into first input of 2-input NOR ||
|8 | Combinational | o21ai | 2-input OR into first input of 2-input NAND ||
|9 | Combinational | o22ai | 2-input OR into both inputs of 2-input NAND ||
|10| Combinational | o21a | 2-input OR into first input of 2-input AND ||
|11| Combinational | o22a | 2-input OR into both inputs of 2-input AND ||
|12| Combinational | or2 | 2-input OR ||
|13| Combinational | or3 | 3-input OR ||
|14| Combinational | xnor2 | 2-input exclusive NOR ||
|15| Combinational | xor2 | 2-input exclusive OR ||
|16| Combinational | a21o | 2-input AND into first input of 2-input OR ||
|17| Combinational | a22o | 2-input AND into both inputs of 2-input OR ||
|18| Combinational | and2 | 2-input AND ||
|19| Combinational | and3 | 3-input AND ||
|20| Buffer | schmittbuf | Schmitt Trigger Buffer ||
|21| Buffer | buf | Buffer ||
|22| Tristate | einvn | Tri-state inverter with negative enable ||
|23| Tristate | einvp | Tri-state inverter with positive enable ||
|24| Delay Flip Flops | dfrbp | Delay flop, inverted reset, complementary outputs ||
|25| Delay Flip Flops | dfrtp | Delay flop, inverted reset, single output ||
|26| Delay Flip Flops | dfsbp | Delay flop, inverted set, complementary outputs ||
|27| Delay Flip Flops | dfstp | Delay flop, inverted set, single output ||
|28| Delay Flip Flops | dfxbp | Delay flop, complementary outputs ||
|29| Delay Flip Flops | dfxtp | Delay flop, single output ||
|30| Delay Flip Flops | dlrtp | Delay latch, inverted reset, non-inverted enable, single output. ||
|31| Delay Flip Flops | dlxtp | Delay latch, non-inverted enable, single output ||
|32| Clock| dlclkp | Clock gate ||
|33| Level Shifting Buffers | lsbufhv2hv_hl | High Voltage to High Voltage, Higher Voltage to Lower Voltage ||
|34| Level Shifting Buffers | lsbufhv2hv_lh | High Voltage to High Voltage, Lower Voltage to Higher Voltage. ||
|35| Level Shifting Buffers | lsbufhv2lv | Low voltage-to-low voltage ||
|36| Level Shifting Buffers | lsbufhv2lv_simple | High Voltage to Low Voltage, simple (hv devices in inverters on lv power rail) ||
|37| Level Shifting Buffers | lsbuflv2hv_clkiso_hlkg | Level-shift clock buffer, low voltage to high voltage, isolated well on input buffer, inverting sleep mode input ||
|38| Level Shifting Buffers | lsbuflv2hv | Low voltage-to-high voltage, isolated well on input buffer, double height cell ||
|39| Level Shifting Buffers | lsbuflv2hv_isosrchvaon | Low voltage to high voltage, isolated well on input buffer, inverting sleep mode input, zero power sleep mode ||
|40| Level Shifting Buffers | lsbuflv2hv_symmetric | Low Voltage to High Voltage, Symmetrical ||
|41|Multiplexers | mux2 | 2-input multiplexer ||
|42|Multiplexers | mux4 | 4-input multiplexer ||
|43| Scan Delay Flip Flop | sdfxtp | Scan delay flop, non-inverted clock, single output ||
|44| Scan Delay Flip Flop | sdfxbp | Scan delay flop, non-inverted clock, complementary outputs ||
|45| Scan Delay Flip Flop | sdfrtp | Scan delay flop, inverted reset, non-inverted clock, single output ||
|46| Scan Delay Flip Flop | sdfrbp | Scan delay flop, inverted reset, non-inverted clock, complementary outputs ||
|47| Scan Delay Flip Flop | sdfstp | Scan delay flop, inverted set, non-inverted clock, single output ||
|48| Scan Delay Flip Flop | sdfsbp | Scan delay flop, inverted set, non-inverted clock, complementary outputs ||
|49| Scan Delay Flip Flop | sdlclkp | Scan gated clock ||
|50| Scan Delay Flip Flop | sdlxtp | No idea ???? ||
|51| Probe | probec_p | Virtual current probe point ||
|52| Probe | probe_p | Virtual voltage probe point ||
|53| Constant | conb | Constant value, low, high outputs ||
|54| Decoupling Capacitor | decap | Decoupling capacitance filler ||
|55| Misc | fill | Fill cell ||
|56| Misc | diode | Antenna tie-down diode | |
