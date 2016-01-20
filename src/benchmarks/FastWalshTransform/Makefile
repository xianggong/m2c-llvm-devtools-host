include ../Makefile.com

all: FastWalshTransform

FastWalshTransform: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim functional ./FastWalshTransform -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./FastWalshTransform -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./FastWalshTransform -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/FastWalshTransform_Kernels.bin

clean:
	rm -rf FastWalshTransform

deepclean:
	rm -rf FastWalshTransform *.bin *.isa *.log
