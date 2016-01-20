include ../Makefile.com

all: BinomialOptionMultiGPU

BinomialOptionMultiGPU: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional ./BinomialOptionMultiGPU -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BinomialOptionMultiGPU -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BinomialOptionMultiGPU -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BinomialOptionMultiGPU_Kernels.bin

clean:
	rm -rf BinomialOptionMultiGPU

deepclean:
	rm -rf BinomialOptionMultiGPU *.bin *.isa *.log
