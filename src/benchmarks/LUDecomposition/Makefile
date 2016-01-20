include ../Makefile.com

all: LUDecomposition

LUDecomposition: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim functional ./LUDecomposition -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./LUDecomposition -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./LUDecomposition -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/LUDecomposition_Kernels.bin

clean:
	rm -rf LUDecomposition

deepclean:
	rm -rf LUDecomposition *.bin *.isa *.log
