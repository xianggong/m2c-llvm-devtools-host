include ../Makefile.com

all: MatrixMultiplication

MatrixMultiplication: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim functional ./MatrixMultiplication -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MatrixMultiplication -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./MatrixMultiplication -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MatrixMultiplication_Kernels.bin

clean:
	rm -rf MatrixMultiplication

deepclean:
	rm -rf MatrixMultiplication *.bin *.isa *.log
