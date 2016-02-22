include ../Makefile.com

all: ScanLargeArrays ScanLargeArrays_ntv

ScanLargeArrays: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

ScanLargeArrays_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim functional ./ScanLargeArrays -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim detailed ./ScanLargeArrays -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./ScanLargeArrays -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace ScanLargeArrays.gz --si-report si.rpt --mem-report mem.rpt ./ScanLargeArrays -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./ScanLargeArrays -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./ScanLargeArrays -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./ScanLargeArrays -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace ScanLargeArrays_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./ScanLargeArrays -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 65536 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim detailed ./ScanLargeArrays -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./ScanLargeArrays -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./ScanLargeArrays_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./ScanLargeArrays -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/ScanLargeArrays_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./ScanLargeArrays -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/ScanLargeArrays_Kernels.bin

clean:
	rm -rf ScanLargeArrays ScanLargeArrays_ntv

deepclean:
	rm -rf ScanLargeArrays ScanLargeArrays_ntv *.bin *.isa *.log debug*
