include ../Makefile.com

all: LUDecomposition LUDecomposition_ntv

LUDecomposition: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

LUDecomposition_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim functional ./LUDecomposition -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim detailed ./LUDecomposition -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./LUDecomposition -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace LUDecomposition.gz --si-report si.rpt --mem-report mem.rpt ./LUDecomposition -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./LUDecomposition -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./LUDecomposition -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./LUDecomposition -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace LUDecomposition_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./LUDecomposition -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim detailed ./LUDecomposition -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./LUDecomposition -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./LUDecomposition_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./LUDecomposition -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/LUDecomposition_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./LUDecomposition -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/LUDecomposition_Kernels.bin

clean:
	rm -rf LUDecomposition LUDecomposition_ntv

deepclean:
	rm -rf LUDecomposition LUDecomposition_ntv *.bin *.isa *.log debug*
