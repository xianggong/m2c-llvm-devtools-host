include ../Makefile.com

all: Template

Template: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim functional ./Template -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./Template -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./Template -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/Template_Kernels.bin

clean:
	rm -rf Template

deepclean:
	rm -rf Template *.bin *.isa *.log
