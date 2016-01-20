include ../Makefile.com

all: TransferOverlap

TransferOverlap: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/TransferOverlap_Kernels.bin $(M2S_BIN) --si-sim functional ./TransferOverlap -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/TransferOverlap_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./TransferOverlap -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/TransferOverlap_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./TransferOverlap -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/TransferOverlap_Kernels.bin

clean:
	rm -rf TransferOverlap

deepclean:
	rm -rf TransferOverlap *.bin *.isa *.log
