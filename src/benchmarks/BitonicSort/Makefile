include ../Makefile.com

all: BitonicSort BitonicSort_ntv

BitonicSort: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BitonicSort_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim functional ./BitonicSort -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim detailed ./BitonicSort -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BitonicSort -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BitonicSort.gz --si-report si.rpt --mem-report mem.rpt ./BitonicSort -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BitonicSort -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BitonicSort -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BitonicSort -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BitonicSort_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BitonicSort -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim detailed ./BitonicSort -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BitonicSort -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BitonicSort_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BitonicSort -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BitonicSort_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BitonicSort -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BitonicSort_Kernels.bin

clean:
	rm -rf BitonicSort BitonicSort_ntv

deepclean:
	rm -rf BitonicSort BitonicSort_ntv *.bin *.isa *.log debug*
