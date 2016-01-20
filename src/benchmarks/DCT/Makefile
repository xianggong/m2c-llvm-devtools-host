include ../Makefile.com

all: DCT

DCT: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim functional ./DCT -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./DCT -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./DCT -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/DCT_Kernels.bin

clean:
	rm -rf DCT

deepclean:
	rm -rf DCT *.bin *.isa *.log
