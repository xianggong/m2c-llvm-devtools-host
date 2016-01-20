include ../Makefile.com

all: Reduction

Reduction: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim functional ./Reduction -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./Reduction -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./Reduction -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/Reduction_Kernels.bin

clean:
	rm -rf Reduction

deepclean:
	rm -rf Reduction *.bin *.isa *.log
