include ../Makefile.com

all: MatrixTranspose MatrixTranspose_ntv

MatrixTranspose: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

MatrixTranspose_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim functional ./MatrixTranspose -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim detailed ./MatrixTranspose -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MatrixTranspose -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MatrixTranspose.gz --si-report si.rpt --mem-report mem.rpt ./MatrixTranspose -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./MatrixTranspose -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MatrixTranspose -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MatrixTranspose -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MatrixTranspose_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./MatrixTranspose -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim detailed ./MatrixTranspose -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MatrixTranspose -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./MatrixTranspose_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MatrixTranspose -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/MatrixTranspose_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./MatrixTranspose -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MatrixTranspose_Kernels.bin

clean:
	rm -rf MatrixTranspose MatrixTranspose_ntv

deepclean:
	rm -rf MatrixTranspose MatrixTranspose_ntv *.bin *.isa *.log debug*
