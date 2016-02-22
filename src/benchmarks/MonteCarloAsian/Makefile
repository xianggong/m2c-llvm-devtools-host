include ../Makefile.com

all: MonteCarloAsian MonteCarloAsian_ntv

MonteCarloAsian: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

MonteCarloAsian_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsian -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsian -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsian -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MonteCarloAsian.gz --si-report si.rpt --mem-report mem.rpt ./MonteCarloAsian -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsian -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsian -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsian -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MonteCarloAsian_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./MonteCarloAsian -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsian -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsian -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./MonteCarloAsian_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MonteCarloAsian -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsian_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./MonteCarloAsian -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MonteCarloAsian_Kernels.bin

clean:
	rm -rf MonteCarloAsian MonteCarloAsian_ntv

deepclean:
	rm -rf MonteCarloAsian MonteCarloAsian_ntv *.bin *.isa *.log debug*
