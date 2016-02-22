include ../Makefile.com

all: HelloWorld HelloWorld_ntv

HelloWorld: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

HelloWorld_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim functional ./HelloWorld -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim detailed ./HelloWorld -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./HelloWorld -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace HelloWorld.gz --si-report si.rpt --mem-report mem.rpt ./HelloWorld -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./HelloWorld -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./HelloWorld -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./HelloWorld -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace HelloWorld_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./HelloWorld -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim detailed ./HelloWorld -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./HelloWorld -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./HelloWorld_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./HelloWorld -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/HelloWorld_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./HelloWorld -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/HelloWorld_Kernels.bin

clean:
	rm -rf HelloWorld HelloWorld_ntv

deepclean:
	rm -rf HelloWorld HelloWorld_ntv *.bin *.isa *.log debug*
