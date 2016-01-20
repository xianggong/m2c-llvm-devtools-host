include ../Makefile.com

all: SobelFilter

SobelFilter: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim functional ./SobelFilter -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./SobelFilter -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./SobelFilter -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/SobelFilter_Kernels.bin

clean:
	rm -rf SobelFilter

deepclean:
	rm -rf SobelFilter *.bin *.isa *.log
