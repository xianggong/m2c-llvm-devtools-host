include ../Makefile.com

all: KernelLaunch

KernelLaunch: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/KernelLaunch_Kernels.bin $(M2S_BIN) --si-sim functional ./KernelLaunch -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/KernelLaunch_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./KernelLaunch -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/KernelLaunch_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./KernelLaunch -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/KernelLaunch_Kernels.bin

clean:
	rm -rf KernelLaunch

deepclean:
	rm -rf KernelLaunch *.bin *.isa *.log
