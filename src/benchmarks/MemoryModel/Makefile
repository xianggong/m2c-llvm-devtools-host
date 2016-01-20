include ../Makefile.com

all: MemoryModel

MemoryModel: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim functional ./MemoryModel -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MemoryModel -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./MemoryModel -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MemoryModel_Kernels.bin

clean:
	rm -rf MemoryModel

deepclean:
	rm -rf MemoryModel *.bin *.isa *.log
