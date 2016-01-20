include ../Makefile.com

all: PrefixSum

PrefixSum: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim functional ./PrefixSum -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./PrefixSum -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./PrefixSum -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/PrefixSum_Kernels.bin

clean:
	rm -rf PrefixSum

deepclean:
	rm -rf PrefixSum *.bin *.isa *.log
