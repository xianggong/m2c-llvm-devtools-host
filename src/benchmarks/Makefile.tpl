include ../Makefile.com

all: EXEC_NAME

EXEC_NAME: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim functional ./EXEC_NAME -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./EXEC_NAME -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./EXEC_NAME -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/EXEC_NAME_Kernels.bin

clean:
	rm -rf EXEC_NAME

deepclean:
	rm -rf EXEC_NAME *.bin *.isa *.log
