include ../Makefile.com

all: AtomicCounters

AtomicCounters: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

run:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim functional ./AtomicCounters -q -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./AtomicCounters -q -e 

optrun:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.opt.bin $(M2S_BIN) --si-sim functional ./AtomicCounters -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/AtomicCounters_Kernels.bin

clean:
	rm -rf AtomicCounters

deepclean:
	rm -rf AtomicCounters *.bin *.isa *.log
