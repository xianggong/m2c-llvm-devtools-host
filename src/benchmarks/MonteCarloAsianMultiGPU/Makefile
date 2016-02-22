include ../Makefile.com

all: MonteCarloAsianMultiGPU MonteCarloAsianMultiGPU_ntv

MonteCarloAsianMultiGPU: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

MonteCarloAsianMultiGPU_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianMultiGPU -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianMultiGPU -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsianMultiGPU -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MonteCarloAsianMultiGPU.gz --si-report si.rpt --mem-report mem.rpt ./MonteCarloAsianMultiGPU -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianMultiGPU -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianMultiGPU -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsianMultiGPU -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MonteCarloAsianMultiGPU_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./MonteCarloAsianMultiGPU -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianMultiGPU -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianMultiGPU -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./MonteCarloAsianMultiGPU_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MonteCarloAsianMultiGPU -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./MonteCarloAsianMultiGPU -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MonteCarloAsianMultiGPU_Kernels.bin

clean:
	rm -rf MonteCarloAsianMultiGPU MonteCarloAsianMultiGPU_ntv

deepclean:
	rm -rf MonteCarloAsianMultiGPU MonteCarloAsianMultiGPU_ntv *.bin *.isa *.log debug*
