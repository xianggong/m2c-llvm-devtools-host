include ../Makefile.com

all: Histogram

Histogram: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim functional ./Histogram -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./Histogram -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./Histogram -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/Histogram_Kernels.bin

clean:
	rm -rf Histogram

deepclean:
	rm -rf Histogram *.bin *.isa *.log
