include ../Makefile.com

all: Histogram Histogram_ntv

Histogram: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

Histogram_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim functional ./Histogram -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim detailed ./Histogram -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./Histogram -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace Histogram.gz --si-report si.rpt --mem-report mem.rpt ./Histogram -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./Histogram -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./Histogram -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./Histogram -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace Histogram_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./Histogram -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim detailed ./Histogram -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./Histogram -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./Histogram_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./Histogram -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/Histogram_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./Histogram -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/Histogram_Kernels.bin

clean:
	rm -rf Histogram Histogram_ntv

deepclean:
	rm -rf Histogram Histogram_ntv *.bin *.isa *.log debug*
