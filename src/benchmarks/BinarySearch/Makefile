include ../Makefile.com

all: BinarySearch BinarySearch_ntv

BinarySearch: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BinarySearch_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim functional ./BinarySearch -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim detailed ./BinarySearch -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BinarySearch -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BinarySearch.gz --si-report si.rpt --mem-report mem.rpt ./BinarySearch -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BinarySearch -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BinarySearch -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BinarySearch -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BinarySearch_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BinarySearch -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim detailed ./BinarySearch -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BinarySearch -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BinarySearch_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BinarySearch -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BinarySearch_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BinarySearch -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BinarySearch_Kernels.bin

clean:
	rm -rf BinarySearch BinarySearch_ntv

deepclean:
	rm -rf BinarySearch BinarySearch_ntv *.bin *.isa *.log debug*
