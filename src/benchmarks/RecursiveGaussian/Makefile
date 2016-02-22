include ../Makefile.com

all: RecursiveGaussian RecursiveGaussian_ntv

RecursiveGaussian: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

RecursiveGaussian_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim functional ./RecursiveGaussian -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim detailed ./RecursiveGaussian -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./RecursiveGaussian -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace RecursiveGaussian.gz --si-report si.rpt --mem-report mem.rpt ./RecursiveGaussian -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./RecursiveGaussian -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./RecursiveGaussian -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./RecursiveGaussian -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace RecursiveGaussian_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./RecursiveGaussian -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim detailed ./RecursiveGaussian -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./RecursiveGaussian -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./RecursiveGaussian_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./RecursiveGaussian -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/RecursiveGaussian_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./RecursiveGaussian -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/RecursiveGaussian_Kernels.bin

clean:
	rm -rf RecursiveGaussian RecursiveGaussian_ntv

deepclean:
	rm -rf RecursiveGaussian RecursiveGaussian_ntv *.bin *.isa *.log debug*
