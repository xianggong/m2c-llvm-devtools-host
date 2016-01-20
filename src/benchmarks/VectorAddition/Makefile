include ../Makefile.com

all: VectorAddition

VectorAddition: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim functional ./VectorAddition -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./VectorAddition -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./VectorAddition -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/VectorAddition_Kernels.bin

clean:
	rm -rf VectorAddition

deepclean:
	rm -rf VectorAddition *.bin *.isa *.log
