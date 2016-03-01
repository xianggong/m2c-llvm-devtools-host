include ../Makefile.com
include ./benchmark.ini

config_files=$(shell ls ../../../conf/)
CONF="default"

all: MonteCarloAsianMultiGPU MonteCarloAsianMultiGPU_ntv

MonteCarloAsianMultiGPU: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ $(LD)

MonteCarloAsianMultiGPU_ntv: *.cpp 
	$(CXX) $? -m32 $(INC) -o $@ -lm -lpthread -lOpenCL

run:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

rundt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

rundtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

runtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace $(CONF)_MonteCarloAsianMultiGPU_Kernels_$(WORKLEN).gz --si-report $(CONF)_si_$(WORKLEN).rpt --mem-report $(CONF)_mem_$(WORKLEN).rpt ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

runsched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

runscheddt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

runscheddtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

runschedtrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace $(CONF)_MonteCarloAsianMultiGPU_Kernels_sched_$(WORKLEN).gz --si-report $(CONF)_si_$(WORKLEN).rpt --mem-report $(CONF)_mem_$(WORKLEN).rpt ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

runfusion:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_fusion.bin $(M2S_BIN) --si-sim functional ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN)

runfusiondt:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_fusion.bin $(M2S_BIN) --si-sim detailed ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN)

runfusiondtcf:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_fusion.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN)

runfusiontrace:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_fusion.bin $(M2S_BIN) --si-sim detailed --si-config $(SI_CONFIG) --mem-config $(MEM_CONFIG) --trace $(CONF)_MonteCarloAsianMultiGPU_Kernels_fusion_$(WORKLEN).gz --si-report $(CONF)_si_$(WORKLEN).rpt --mem-report $(CONF)_mem_$(WORKLEN).rpt ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN)

scale:
	len=$(MIN_LEN) ; while [[ $$len -le $(MAX_LEN) ]] ; do \
                $(MAKE) runtrace RUNOPT= WORKLEN=$$len ; \
                $(MAKE) runschedtrace RUNOPT= WORKLEN=$$len ; \
                $(MAKE) runfusiontrace RUNOPT= WORKLEN=$$len ; \
                ((len = len * 2 )); \
        done

scaleconf:
	for conf in $(config_files); do \
                $(MAKE) scale SI_CONFIG=../../../conf/$$conf/si-config MEM_CONFIG=../../../conf/$$conf/mem-config CONF=$$conf; \
        done

rnt:
	./MonteCarloAsianMultiGPU_ntv -e 

isa:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.isa ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

isasched:
	M2S_OPENCL_BINARY=$(PWD)/MonteCarloAsianMultiGPU_Kernels_sched.bin $(M2S_BIN) --si-sim functional --si-debug-isa debug.sched.isa ./MonteCarloAsianMultiGPU -q $(RUNOPT) -x $(WORKLEN) 

disasm:
	$(M2S_BIN) --si-disasm $(PWD)/MonteCarloAsianMultiGPU_Kernels.bin

clean:
	rm -rf MonteCarloAsianMultiGPU MonteCarloAsianMultiGPU_ntv *.isa *.log debug* *.rpt *.gz

deepclean:
	rm -rf MonteCarloAsianMultiGPU MonteCarloAsianMultiGPU_ntv *.bin *.isa *.log debug* *.rpt *.gz
