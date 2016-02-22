include ../../../Makefile.inc

all: exe_src exe_src_m2s 

exe_src: RemainderDivide.c
	$(CC) $(CC_FLAG) -g $< -o exe_src $(CC_INC) $(CC_LIB) 

exe_src_m2s: RemainderDivide.c
	$(CC) $(CC_FLAG) -m32 $< -o exe_src_m2s $(CC_INC) -L $(M2S_LIB) -lm2s-opencl

run:
	M2S_OPENCL_BINARY=./RemainderDivide.bin $(M2S) --si-sim functional ./exe_src_m2s 

rundbg:
	M2S_OPENCL_BINARY=./RemainderDivide.bin $(M2S) --si-sim functional --si-debug-isa sidebug.isa ./exe_src_m2s 

run_native:
	./exe_src 

deepclean:
	rm -rf exe_src exe_src_m2s *.log *.gz

clean:
	rm -rf exe_src exe_src_m2s 
