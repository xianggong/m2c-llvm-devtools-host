include ../Makefile.com

all: StringSearch

StringSearch: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim functional ./StringSearch -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./StringSearch -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./StringSearch -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/StringSearch_Kernels.bin

clean:
	rm -rf StringSearch

deepclean:
	rm -rf StringSearch *.bin *.isa *.log
