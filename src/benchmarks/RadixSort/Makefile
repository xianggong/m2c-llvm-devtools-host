include ../Makefile.com

all: RadixSort

RadixSort: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim functional ./RadixSort -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./RadixSort -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./RadixSort -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/RadixSort_Kernels.bin

clean:
	rm -rf RadixSort

deepclean:
	rm -rf RadixSort *.bin *.isa *.log
