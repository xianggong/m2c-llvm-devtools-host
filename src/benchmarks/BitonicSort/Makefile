include ../Makefile.com

all: BitonicSort

BitonicSort: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim functional ./BitonicSort -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BitonicSort -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BitonicSort -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BitonicSort_Kernels.bin

clean:
	rm -rf BitonicSort

deepclean:
	rm -rf BitonicSort *.bin *.isa *.log
