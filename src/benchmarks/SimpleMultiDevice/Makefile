include ../Makefile.com

all: SimpleMultiDevice SimpleMultiDevice_ntv

SimpleMultiDevice: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

SimpleMultiDevice_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim functional ./SimpleMultiDevice -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim detailed ./SimpleMultiDevice -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./SimpleMultiDevice -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace SimpleMultiDevice.gz --si-report si.rpt --mem-report mem.rpt ./SimpleMultiDevice -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./SimpleMultiDevice -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./SimpleMultiDevice -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./SimpleMultiDevice -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace SimpleMultiDevice_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./SimpleMultiDevice -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim detailed ./SimpleMultiDevice -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./SimpleMultiDevice -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./SimpleMultiDevice_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./SimpleMultiDevice -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/SimpleMultiDevice_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./SimpleMultiDevice -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/SimpleMultiDevice_Kernels.bin

clean:
	rm -rf SimpleMultiDevice SimpleMultiDevice_ntv

deepclean:
	rm -rf SimpleMultiDevice SimpleMultiDevice_ntv *.bin *.isa *.log debug*
