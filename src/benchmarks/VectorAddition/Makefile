include ../Makefile.com

all: VectorAddition VectorAddition_ntv

VectorAddition: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

VectorAddition_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim functional ./VectorAddition -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim detailed ./VectorAddition -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./VectorAddition -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace VectorAddition.gz --si-report si.rpt --mem-report mem.rpt ./VectorAddition -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./VectorAddition -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./VectorAddition -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./VectorAddition -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace VectorAddition_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./VectorAddition -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim detailed ./VectorAddition -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./VectorAddition -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./VectorAddition_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./VectorAddition -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/VectorAddition_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./VectorAddition -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/VectorAddition_Kernels.bin

clean:
	rm -rf VectorAddition VectorAddition_ntv

deepclean:
	rm -rf VectorAddition VectorAddition_ntv *.bin *.isa *.log debug*
