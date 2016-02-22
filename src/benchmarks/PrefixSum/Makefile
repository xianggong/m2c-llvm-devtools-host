include ../Makefile.com

all: PrefixSum PrefixSum_ntv

PrefixSum: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

PrefixSum_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim functional ./PrefixSum -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim detailed ./PrefixSum -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./PrefixSum -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace PrefixSum.gz --si-report si.rpt --mem-report mem.rpt ./PrefixSum -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./PrefixSum -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./PrefixSum -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./PrefixSum -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace PrefixSum_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./PrefixSum -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim detailed ./PrefixSum -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./PrefixSum -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./PrefixSum_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./PrefixSum -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/PrefixSum_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./PrefixSum -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/PrefixSum_Kernels.bin

clean:
	rm -rf PrefixSum PrefixSum_ntv

deepclean:
	rm -rf PrefixSum PrefixSum_ntv *.bin *.isa *.log debug*
