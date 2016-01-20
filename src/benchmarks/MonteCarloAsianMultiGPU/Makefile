include ../Makefile.com

all: MonteCarloAsianMultiGPU

MonteCarloAsianMultiGPU: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianMultiGPU -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MonteCarloAsianMultiGPU -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianMultiGPU -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MonteCarloAsianMultiGPU_Kernels.bin

clean:
	rm -rf MonteCarloAsianMultiGPU

deepclean:
	rm -rf MonteCarloAsianMultiGPU *.bin *.isa *.log
