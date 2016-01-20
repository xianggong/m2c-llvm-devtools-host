include ../Makefile.com

all: DeviceFission11Ext

DeviceFission11Ext: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim functional ./DeviceFission11Ext -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./DeviceFission11Ext -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./DeviceFission11Ext -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/DeviceFission11Ext_Kernels.bin

clean:
	rm -rf DeviceFission11Ext

deepclean:
	rm -rf DeviceFission11Ext *.bin *.isa *.log
