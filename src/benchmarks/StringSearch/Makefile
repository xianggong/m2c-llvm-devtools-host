include ../Makefile.com

all: StringSearch StringSearch_ntv

StringSearch: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

StringSearch_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim functional ./StringSearch -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim detailed ./StringSearch -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./StringSearch -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace StringSearch.gz --si-report si.rpt --mem-report mem.rpt ./StringSearch -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./StringSearch -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./StringSearch -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./StringSearch -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace StringSearch_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./StringSearch -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim detailed ./StringSearch -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./StringSearch -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./StringSearch_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./StringSearch -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/StringSearch_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./StringSearch -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/StringSearch_Kernels.bin

clean:
	rm -rf StringSearch StringSearch_ntv

deepclean:
	rm -rf StringSearch StringSearch_ntv *.bin *.isa *.log debug*
