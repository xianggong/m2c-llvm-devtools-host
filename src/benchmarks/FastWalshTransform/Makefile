include ../Makefile.com

all: FastWalshTransform FastWalshTransform_ntv

FastWalshTransform: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

FastWalshTransform_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim functional ./FastWalshTransform -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim detailed ./FastWalshTransform -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./FastWalshTransform -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace FastWalshTransform.gz --si-report si.rpt --mem-report mem.rpt ./FastWalshTransform -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./FastWalshTransform -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./FastWalshTransform -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./FastWalshTransform -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace FastWalshTransform_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./FastWalshTransform -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim detailed ./FastWalshTransform -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./FastWalshTransform -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./FastWalshTransform_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./FastWalshTransform -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/FastWalshTransform_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./FastWalshTransform -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/FastWalshTransform_Kernels.bin

clean:
	rm -rf FastWalshTransform FastWalshTransform_ntv

deepclean:
	rm -rf FastWalshTransform FastWalshTransform_ntv *.bin *.isa *.log debug*
