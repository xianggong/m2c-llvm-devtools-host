include ../Makefile.com

all: SimpleConvolution SimpleConvolution_ntv

SimpleConvolution: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

SimpleConvolution_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim functional ./SimpleConvolution -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim detailed ./SimpleConvolution -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./SimpleConvolution -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace SimpleConvolution.gz --si-report si.rpt --mem-report mem.rpt ./SimpleConvolution -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./SimpleConvolution -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./SimpleConvolution -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./SimpleConvolution -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace SimpleConvolution_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./SimpleConvolution -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim detailed ./SimpleConvolution -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./SimpleConvolution -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./SimpleConvolution_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./SimpleConvolution -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/SimpleConvolution_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./SimpleConvolution -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/SimpleConvolution_Kernels.bin

clean:
	rm -rf SimpleConvolution SimpleConvolution_ntv

deepclean:
	rm -rf SimpleConvolution SimpleConvolution_ntv *.bin *.isa *.log debug*
