include ../Makefile.com

all: SimpleConvolution

SimpleConvolution: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim functional ./SimpleConvolution -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./SimpleConvolution -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./SimpleConvolution -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/SimpleConvolution_Kernels.bin

clean:
	rm -rf SimpleConvolution

deepclean:
	rm -rf SimpleConvolution *.bin *.isa *.log
