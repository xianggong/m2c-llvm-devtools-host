include ../Makefile.com

all: RadixSort RadixSort_ntv

RadixSort: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

RadixSort_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim functional ./RadixSort -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim detailed ./RadixSort -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./RadixSort -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace RadixSort.gz --si-report si.rpt --mem-report mem.rpt ./RadixSort -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./RadixSort -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./RadixSort -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./RadixSort -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace RadixSort_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./RadixSort -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim detailed ./RadixSort -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./RadixSort -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./RadixSort_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./RadixSort -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/RadixSort_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./RadixSort -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/RadixSort_Kernels.bin

clean:
	rm -rf RadixSort RadixSort_ntv

deepclean:
	rm -rf RadixSort RadixSort_ntv *.bin *.isa *.log debug*
