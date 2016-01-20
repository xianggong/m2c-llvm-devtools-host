include ../Makefile.com

all: BlackScholesDP

BlackScholesDP: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim functional ./BlackScholesDP -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BlackScholesDP -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BlackScholesDP -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BlackScholesDP_Kernels.bin

clean:
	rm -rf BlackScholesDP

deepclean:
	rm -rf BlackScholesDP *.bin *.isa *.log
