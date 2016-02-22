include ../Makefile.com

all: BoxFilter BoxFilter_ntv

BoxFilter: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BoxFilter_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim functional ./BoxFilter -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim detailed ./BoxFilter -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BoxFilter -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BoxFilter.gz --si-report si.rpt --mem-report mem.rpt ./BoxFilter -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BoxFilter -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BoxFilter -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BoxFilter -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BoxFilter_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BoxFilter -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim detailed ./BoxFilter -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BoxFilter -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BoxFilter_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BoxFilter -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BoxFilter_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BoxFilter -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BoxFilter_Kernels.bin

clean:
	rm -rf BoxFilter BoxFilter_ntv

deepclean:
	rm -rf BoxFilter BoxFilter_ntv *.bin *.isa *.log debug*
