include ../Makefile.com

all: DCT DCT_ntv

DCT: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

DCT_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim functional ./DCT -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim detailed ./DCT -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./DCT -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace DCT.gz --si-report si.rpt --mem-report mem.rpt ./DCT -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./DCT -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./DCT -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./DCT -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace DCT_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./DCT -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim detailed ./DCT -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./DCT -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./DCT_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./DCT -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/DCT_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./DCT -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/DCT_Kernels.bin

clean:
	rm -rf DCT DCT_ntv

deepclean:
	rm -rf DCT DCT_ntv *.bin *.isa *.log debug*
