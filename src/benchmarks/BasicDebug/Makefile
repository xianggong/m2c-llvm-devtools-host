include ../Makefile.com

all: BasicDebug

BasicDebug: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim functional ./BasicDebug -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BasicDebug -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BasicDebug -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BasicDebug_Kernels.bin

clean:
	rm -rf BasicDebug

deepclean:
	rm -rf BasicDebug *.bin *.isa *.log
