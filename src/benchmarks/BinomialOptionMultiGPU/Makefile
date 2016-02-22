include ../Makefile.com

all: BinomialOptionMultiGPU BinomialOptionMultiGPU_ntv

BinomialOptionMultiGPU: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

BinomialOptionMultiGPU_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional ./BinomialOptionMultiGPU -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed ./BinomialOptionMultiGPU -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BinomialOptionMultiGPU -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BinomialOptionMultiGPU.gz --si-report si.rpt --mem-report mem.rpt ./BinomialOptionMultiGPU -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./BinomialOptionMultiGPU -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BinomialOptionMultiGPU -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./BinomialOptionMultiGPU -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace BinomialOptionMultiGPU_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./BinomialOptionMultiGPU -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed ./BinomialOptionMultiGPU -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./BinomialOptionMultiGPU -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./BinomialOptionMultiGPU_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./BinomialOptionMultiGPU -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/BinomialOptionMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./BinomialOptionMultiGPU -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/BinomialOptionMultiGPU_Kernels.bin

clean:
	rm -rf BinomialOptionMultiGPU BinomialOptionMultiGPU_ntv

deepclean:
	rm -rf BinomialOptionMultiGPU BinomialOptionMultiGPU_ntv *.bin *.isa *.log debug*
