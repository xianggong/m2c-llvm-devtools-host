include ../Makefile.com

all: BinomialOption BinomialOption_ntv

BinomialOption: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BinomialOption_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim functional ./BinomialOption -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim detailed ./BinomialOption -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BinomialOption -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BinomialOption.gz --si-report si.rpt --mem-report mem.rpt ./BinomialOption -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BinomialOption -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BinomialOption -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BinomialOption -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BinomialOption_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BinomialOption -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim detailed ./BinomialOption -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BinomialOption -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BinomialOption_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BinomialOption -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOption_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BinomialOption -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BinomialOption_Kernels.bin

clean:
	rm -rf BinomialOption BinomialOption_ntv

deepclean:
	rm -rf BinomialOption BinomialOption_ntv *.bin *.isa *.log debug*
