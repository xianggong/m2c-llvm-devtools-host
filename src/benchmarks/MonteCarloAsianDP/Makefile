include ../Makefile.com

all: MonteCarloAsianDP MonteCarloAsianDP_ntv

MonteCarloAsianDP: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

MonteCarloAsianDP_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianDP -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianDP -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsianDP -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MonteCarloAsianDP.gz --si-report si.rpt --mem-report mem.rpt ./MonteCarloAsianDP -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianDP -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianDP -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsianDP -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MonteCarloAsianDP_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./MonteCarloAsianDP -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianDP -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianDP -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./MonteCarloAsianDP_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MonteCarloAsianDP -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianDP_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./MonteCarloAsianDP -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MonteCarloAsianDP_Kernels.bin

clean:
	rm -rf MonteCarloAsianDP MonteCarloAsianDP_ntv

deepclean:
	rm -rf MonteCarloAsianDP MonteCarloAsianDP_ntv *.bin *.isa *.log debug*
