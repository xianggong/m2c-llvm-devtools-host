include ../Makefile.com

all: URNG

URNG: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim functional ./URNG -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./URNG -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./URNG -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/URNG_Kernels.bin

clean:
	rm -rf URNG

deepclean:
	rm -rf URNG *.bin *.isa *.log
