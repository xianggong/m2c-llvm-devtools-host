include ../Makefile.com

all: RecursiveGaussian

RecursiveGaussian: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim functional ./RecursiveGaussian -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./RecursiveGaussian -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./RecursiveGaussian -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/RecursiveGaussian_Kernels.bin

clean:
	rm -rf RecursiveGaussian

deepclean:
	rm -rf RecursiveGaussian *.bin *.isa *.log
