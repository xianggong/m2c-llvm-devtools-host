include ../Makefile.com

all: MonteCarloAsian

MonteCarloAsian: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsian -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MonteCarloAsian -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsian -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MonteCarloAsian_Kernels.bin

clean:
	rm -rf MonteCarloAsian

deepclean:
	rm -rf MonteCarloAsian *.bin *.isa *.log
