include ../Makefile.com

all: FloydWarshall FloydWarshall_ntv

FloydWarshall: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

FloydWarshall_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim functional ./FloydWarshall -q -e 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim detailed ./FloydWarshall -q -e 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./FloydWarshall -q -e 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace FloydWarshall.gz --si-report si.rpt --mem-report mem.rpt ./FloydWarshall -q -e 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./FloydWarshall -q -e 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./FloydWarshall -q -e 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./FloydWarshall -q -e 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace FloydWarshall_sched.gz --si-report sisched.rpt --mem-report memsched.rpt ./FloydWarshall -q -e 

scale:
	rm -f debug.scale; \
        len=1 ; while [[ $$len -le 4096 ]] ; do \
                echo $$len ; \
                echo "default:" ; \
                M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim detailed ./FloydWarshall -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                echo "sisched:" ; \
                M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./FloydWarshall -q -e -x $$len 2>&1 | grep "Cycles =" ; \
                ((len = len * 2 )); \
        done

rnt:
	./FloydWarshall_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./FloydWarshall -q -e 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/FloydWarshall_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./FloydWarshall -q -e 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/FloydWarshall_Kernels.bin

clean:
	rm -rf FloydWarshall FloydWarshall_ntv

deepclean:
	rm -rf FloydWarshall FloydWarshall_ntv *.bin *.isa *.log debug*
