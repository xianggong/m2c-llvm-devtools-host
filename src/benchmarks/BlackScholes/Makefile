include ../Makefile.com

all: BlackScholes BlackScholes_ntv

BlackScholes: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BlackScholes_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim functional ./BlackScholes -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim detailed ./BlackScholes -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BlackScholes -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BlackScholes.gz --si-report si.rpt --mem-report mem.rpt ./BlackScholes -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BlackScholes -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BlackScholes -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BlackScholes -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BlackScholes_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BlackScholes -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim detailed ./BlackScholes -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BlackScholes -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BlackScholes_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BlackScholes -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholes_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BlackScholes -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BlackScholes_Kernels.bin

clean:
	rm -rf BlackScholes BlackScholes_ntv

deepclean:
	rm -rf BlackScholes BlackScholes_ntv *.bin *.isa *.log debug*
