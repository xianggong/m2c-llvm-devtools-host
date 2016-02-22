include ../Makefile.com

all: URNG URNG_ntv

URNG: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

URNG_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim functional ./URNG -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim detailed ./URNG -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./URNG -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace URNG.gz --si-report si.rpt --mem-report mem.rpt ./URNG -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./URNG -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./URNG -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./URNG -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace URNG_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./URNG -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim detailed ./URNG -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./URNG -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./URNG_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./URNG -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/URNG_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./URNG -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/URNG_Kernels.bin

clean:
	rm -rf URNG URNG_ntv

deepclean:
	rm -rf URNG URNG_ntv *.bin *.isa *.log debug*
