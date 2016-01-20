include ../Makefile.com

all: MatrixTranspose

MatrixTranspose: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim functional ./MatrixTranspose -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MatrixTranspose -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./MatrixTranspose -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MatrixTranspose_Kernels.bin

clean:
	rm -rf MatrixTranspose

deepclean:
	rm -rf MatrixTranspose *.bin *.isa *.log
