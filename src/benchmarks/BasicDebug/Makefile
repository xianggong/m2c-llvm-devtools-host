include ../Makefile.com

all: BasicDebug BasicDebug_ntv

BasicDebug: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BasicDebug_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim functional ./BasicDebug -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim detailed ./BasicDebug -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BasicDebug -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BasicDebug.gz --si-report si.rpt --mem-report mem.rpt ./BasicDebug -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BasicDebug -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BasicDebug -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BasicDebug -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BasicDebug_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BasicDebug -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim detailed ./BasicDebug -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BasicDebug -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BasicDebug_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BasicDebug -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BasicDebug_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BasicDebug -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BasicDebug_Kernels.bin

clean:
	rm -rf BasicDebug BasicDebug_ntv

deepclean:
	rm -rf BasicDebug BasicDebug_ntv *.bin *.isa *.log debug*
