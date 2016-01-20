include ../Makefile.com

all: ScanLargeArrays

ScanLargeArrays: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim functional ./ScanLargeArrays -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./ScanLargeArrays -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./ScanLargeArrays -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/ScanLargeArrays_Kernels.bin

clean:
	rm -rf ScanLargeArrays

deepclean:
	rm -rf ScanLargeArrays *.bin *.isa *.log
