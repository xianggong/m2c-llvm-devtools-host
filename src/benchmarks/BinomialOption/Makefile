include ../Makefile.com

all: BinomialOption

BinomialOption: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim functional ./BinomialOption -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BinomialOption -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./BinomialOption -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BinomialOption_Kernels.bin

clean:
	rm -rf BinomialOption

deepclean:
	rm -rf BinomialOption *.bin *.isa *.log
