include ../Makefile.com

all: Template Template_ntv

Template: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

Template_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim functional ./Template -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim detailed ./Template -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./Template -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace Template.gz --si-report si.rpt --mem-report mem.rpt ./Template -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./Template -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./Template -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./Template -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace Template_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./Template -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim detailed ./Template -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/Template_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./Template -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./Template_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./Template -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/Template_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./Template -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/Template_Kernels.bin

clean:
	rm -rf Template Template_ntv

deepclean:
	rm -rf Template Template_ntv *.bin *.isa *.log debug*
