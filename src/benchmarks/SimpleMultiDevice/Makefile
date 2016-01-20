include ../Makefile.com

all: SimpleMultiDevice

SimpleMultiDevice: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim functional ./SimpleMultiDevice -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./SimpleMultiDevice -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./SimpleMultiDevice -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/SimpleMultiDevice_Kernels.bin

clean:
	rm -rf SimpleMultiDevice

deepclean:
	rm -rf SimpleMultiDevice *.bin *.isa *.log
