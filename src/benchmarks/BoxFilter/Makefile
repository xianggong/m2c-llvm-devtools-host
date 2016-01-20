include ../Makefile.com

all: BoxFilter

BoxFilter: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim functional ./BoxFilter -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BoxFilter -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BoxFilter -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BoxFilter_Kernels.bin

clean:
	rm -rf BoxFilter

deepclean:
	rm -rf BoxFilter *.bin *.isa *.log
