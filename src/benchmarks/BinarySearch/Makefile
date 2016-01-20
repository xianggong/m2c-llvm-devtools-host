include ../Makefile.com

all: BinarySearch

BinarySearch: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim functional ./BinarySearch -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BinarySearch -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BinarySearch -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BinarySearch_Kernels.bin

clean:
	rm -rf BinarySearch

deepclean:
	rm -rf BinarySearch *.bin *.isa *.log
