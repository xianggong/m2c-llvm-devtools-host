include ../Makefile.com

all: SobelFilter SobelFilter_ntv

SobelFilter: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

SobelFilter_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim functional ./SobelFilter -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim detailed ./SobelFilter -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./SobelFilter -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace SobelFilter.gz --si-report si.rpt --mem-report mem.rpt ./SobelFilter -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./SobelFilter -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./SobelFilter -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./SobelFilter -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace SobelFilter_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./SobelFilter -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim detailed ./SobelFilter -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./SobelFilter -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./SobelFilter_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./SobelFilter -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/SobelFilter_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./SobelFilter -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/SobelFilter_Kernels.bin

clean:
	rm -rf SobelFilter SobelFilter_ntv

deepclean:
	rm -rf SobelFilter SobelFilter_ntv *.bin *.isa *.log debug*
