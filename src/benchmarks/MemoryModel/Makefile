include ../Makefile.com

all: MemoryModel MemoryModel_ntv

MemoryModel: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

MemoryModel_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim functional ./MemoryModel -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim detailed ./MemoryModel -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MemoryModel -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MemoryModel.gz --si-report si.rpt --mem-report mem.rpt ./MemoryModel -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./MemoryModel -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MemoryModel -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MemoryModel -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace MemoryModel_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./MemoryModel -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim detailed ./MemoryModel -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MemoryModel -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./MemoryModel_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MemoryModel -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/MemoryModel_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./MemoryModel -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MemoryModel_Kernels.bin

clean:
	rm -rf MemoryModel MemoryModel_ntv

deepclean:
	rm -rf MemoryModel MemoryModel_ntv *.bin *.isa *.log debug*
