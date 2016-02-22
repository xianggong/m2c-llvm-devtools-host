include ../Makefile.com

all: MatrixMultiplication MatrixMultiplication_ntv

MatrixMultiplication: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

MatrixMultiplication_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim functional ./MatrixMultiplication -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim detailed ./MatrixMultiplication -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MatrixMultiplication -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MatrixMultiplication.gz --si-report si.rpt --mem-report mem.rpt ./MatrixMultiplication -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./MatrixMultiplication -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MatrixMultiplication -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MatrixMultiplication -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MatrixMultiplication_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./MatrixMultiplication -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim detailed ./MatrixMultiplication -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MatrixMultiplication -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./MatrixMultiplication_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MatrixMultiplication -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/MatrixMultiplication_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./MatrixMultiplication -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MatrixMultiplication_Kernels.bin

clean:
	rm -rf MatrixMultiplication MatrixMultiplication_ntv

deepclean:
	rm -rf MatrixMultiplication MatrixMultiplication_ntv *.bin *.isa *.log debug*
