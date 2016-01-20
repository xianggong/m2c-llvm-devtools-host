include ../Makefile.com

all: MonteCarloAsianDP

MonteCarloAsianDP: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianDP -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MonteCarloAsianDP -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianDP -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MonteCarloAsianDP_Kernels.bin

clean:
	rm -rf MonteCarloAsianDP

deepclean:
	rm -rf MonteCarloAsianDP *.bin *.isa *.log
