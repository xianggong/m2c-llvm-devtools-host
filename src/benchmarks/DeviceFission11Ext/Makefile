include ../Makefile.com

all: DeviceFission11Ext DeviceFission11Ext_ntv

DeviceFission11Ext: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

DeviceFission11Ext_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim functional ./DeviceFission11Ext -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim detailed ./DeviceFission11Ext -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./DeviceFission11Ext -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace DeviceFission11Ext.gz --si-report si.rpt --mem-report mem.rpt ./DeviceFission11Ext -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./DeviceFission11Ext -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./DeviceFission11Ext -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./DeviceFission11Ext -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace DeviceFission11Ext_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./DeviceFission11Ext -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim detailed ./DeviceFission11Ext -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./DeviceFission11Ext -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./DeviceFission11Ext_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./DeviceFission11Ext -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/DeviceFission11Ext_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./DeviceFission11Ext -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/DeviceFission11Ext_Kernels.bin

clean:
	rm -rf DeviceFission11Ext DeviceFission11Ext_ntv

deepclean:
	rm -rf DeviceFission11Ext DeviceFission11Ext_ntv *.bin *.isa *.log debug*
