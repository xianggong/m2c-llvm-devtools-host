include ../Makefile.com

all: AtomicCounters AtomicCounters_ntv

AtomicCounters: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

AtomicCounters_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim functional ./AtomicCounters -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim detailed ./AtomicCounters -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./AtomicCounters -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace AtomicCounters.gz --si-report si.rpt --mem-report mem.rpt ./AtomicCounters -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./AtomicCounters -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./AtomicCounters -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./AtomicCounters -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace AtomicCounters_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./AtomicCounters -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim detailed ./AtomicCounters -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./AtomicCounters -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./AtomicCounters_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./AtomicCounters -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/AtomicCounters_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./AtomicCounters -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/AtomicCounters_Kernels.bin

clean:
	rm -rf AtomicCounters AtomicCounters_ntv

deepclean:
	rm -rf AtomicCounters AtomicCounters_ntv *.bin *.isa *.log debug*
