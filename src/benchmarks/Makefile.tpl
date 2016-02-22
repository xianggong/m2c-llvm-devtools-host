include ../Makefile.com

all: EXEC_NAME EXEC_NAME_ntv

EXEC_NAME: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

EXEC_NAME_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim functional ./EXEC_NAME -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim detailed ./EXEC_NAME -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./EXEC_NAME -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace EXEC_NAME.gz --si-report si.rpt --mem-report mem.rpt ./EXEC_NAME -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./EXEC_NAME -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./EXEC_NAME -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./EXEC_NAME -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace EXEC_NAME_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./EXEC_NAME -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim detailed ./EXEC_NAME -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./EXEC_NAME -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./EXEC_NAME_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./EXEC_NAME -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/EXEC_NAME_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./EXEC_NAME -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/EXEC_NAME_Kernels.bin

clean:
	rm -rf EXEC_NAME EXEC_NAME_ntv

deepclean:
	rm -rf EXEC_NAME EXEC_NAME_ntv *.bin *.isa *.log debug*
