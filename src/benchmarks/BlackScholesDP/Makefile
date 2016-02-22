include ../Makefile.com

all: BlackScholesDP BlackScholesDP_ntv

BlackScholesDP: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BlackScholesDP_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim functional ./BlackScholesDP -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim detailed ./BlackScholesDP -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BlackScholesDP -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BlackScholesDP.gz --si-report si.rpt --mem-report mem.rpt ./BlackScholesDP -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BlackScholesDP -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BlackScholesDP -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BlackScholesDP -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BlackScholesDP_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BlackScholesDP -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim detailed ./BlackScholesDP -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BlackScholesDP -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BlackScholesDP_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BlackScholesDP -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BlackScholesDP_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BlackScholesDP -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BlackScholesDP_Kernels.bin

clean:
	rm -rf BlackScholesDP BlackScholesDP_ntv

deepclean:
	rm -rf BlackScholesDP BlackScholesDP_ntv *.bin *.isa *.log debug*
