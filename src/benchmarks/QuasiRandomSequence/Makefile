include ../Makefile.com

all: QuasiRandomSequence QuasiRandomSequence_ntv

QuasiRandomSequence: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

QuasiRandomSequence_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim functional ./QuasiRandomSequence -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim detailed ./QuasiRandomSequence -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./QuasiRandomSequence -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace QuasiRandomSequence.gz --si-report si.rpt --mem-report mem.rpt ./QuasiRandomSequence -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./QuasiRandomSequence -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./QuasiRandomSequence -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./QuasiRandomSequence -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace QuasiRandomSequence_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./QuasiRandomSequence -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim detailed ./QuasiRandomSequence -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./QuasiRandomSequence -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./QuasiRandomSequence_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./QuasiRandomSequence -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/QuasiRandomSequence_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./QuasiRandomSequence -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/QuasiRandomSequence_Kernels.bin

clean:
	rm -rf QuasiRandomSequence QuasiRandomSequence_ntv

deepclean:
	rm -rf QuasiRandomSequence QuasiRandomSequence_ntv *.bin *.isa *.log debug*
