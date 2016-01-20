include ../Makefile.com

all: FloydWarshall

FloydWarshall: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim functional ./FloydWarshall -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./FloydWarshall -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./FloydWarshall -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/FloydWarshall_Kernels.bin

clean:
	rm -rf FloydWarshall

deepclean:
	rm -rf FloydWarshall *.bin *.isa *.log
