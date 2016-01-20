include ../Makefile.com

all: BlackScholes

BlackScholes: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim functional ./BlackScholes -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BlackScholes -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BlackScholes -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BlackScholes_Kernels.bin

clean:
	rm -rf BlackScholes

deepclean:
	rm -rf BlackScholes *.bin *.isa *.log
