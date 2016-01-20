include ../Makefile.com

all: DwtHaar1D

DwtHaar1D: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim functional ./DwtHaar1D -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./DwtHaar1D -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./DwtHaar1D -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/DwtHaar1D_Kernels.bin

clean:
	rm -rf DwtHaar1D

deepclean:
	rm -rf DwtHaar1D *.bin *.isa *.log
