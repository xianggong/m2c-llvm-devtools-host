include ../Makefile.com

all: DynamicOpenCLDetection

DynamicOpenCLDetection: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/DynamicOpenCLDetection_Kernels.bin $(M2S_BIN) --si-sim functional ./DynamicOpenCLDetection -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/DynamicOpenCLDetection_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./DynamicOpenCLDetection -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/DynamicOpenCLDetection_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./DynamicOpenCLDetection -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/DynamicOpenCLDetection_Kernels.bin

clean:
	rm -rf DynamicOpenCLDetection

deepclean:
	rm -rf DynamicOpenCLDetection *.bin *.isa *.log
