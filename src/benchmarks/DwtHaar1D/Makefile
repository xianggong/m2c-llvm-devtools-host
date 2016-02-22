include ../Makefile.com

all: DwtHaar1D DwtHaar1D_ntv

DwtHaar1D: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

DwtHaar1D_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim functional ./DwtHaar1D -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim detailed ./DwtHaar1D -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./DwtHaar1D -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace DwtHaar1D.gz --si-report si.rpt --mem-report mem.rpt ./DwtHaar1D -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./DwtHaar1D -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./DwtHaar1D -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./DwtHaar1D -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace DwtHaar1D_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./DwtHaar1D -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim detailed ./DwtHaar1D -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./DwtHaar1D -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./DwtHaar1D_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./DwtHaar1D -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/DwtHaar1D_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./DwtHaar1D -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/DwtHaar1D_Kernels.bin

clean:
	rm -rf DwtHaar1D DwtHaar1D_ntv

deepclean:
	rm -rf DwtHaar1D DwtHaar1D_ntv *.bin *.isa *.log debug*
