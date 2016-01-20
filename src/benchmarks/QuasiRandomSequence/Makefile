include ../Makefile.com

all: QuasiRandomSequence

QuasiRandomSequence: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim functional ./QuasiRandomSequence -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./QuasiRandomSequence -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./QuasiRandomSequence -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/QuasiRandomSequence_Kernels.bin

clean:
	rm -rf QuasiRandomSequence

deepclean:
	rm -rf QuasiRandomSequence *.bin *.isa *.log
