include ../Makefile.com

all: HelloWorld

HelloWorld: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim functional ./HelloWorld -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./HelloWorld -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./HelloWorld -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/HelloWorld_Kernels.bin

clean:
	rm -rf HelloWorld

deepclean:
	rm -rf HelloWorld *.bin *.isa *.log
