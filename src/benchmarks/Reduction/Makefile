include ../Makefile.com

all: Reduction Reduction_ntv

Reduction: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

Reduction_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim functional ./Reduction -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim detailed ./Reduction -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./Reduction -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace Reduction.gz --si-report si.rpt --mem-report mem.rpt ./Reduction -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./Reduction -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./Reduction -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./Reduction -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace Reduction_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./Reduction -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim detailed ./Reduction -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./Reduction -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./Reduction_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./Reduction -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/Reduction_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./Reduction -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/Reduction_Kernels.bin

clean:
	rm -rf Reduction Reduction_ntv

deepclean:
	rm -rf Reduction Reduction_ntv *.bin *.isa *.log debug*
