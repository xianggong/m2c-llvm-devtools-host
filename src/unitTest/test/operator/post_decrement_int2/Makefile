include ../../../Makefile.inc

all: exentv exem2s

exentv:
	@-$(CC) $(CC_FLAG) *src.c -o exentv $(CC_INC) $(CC_LIB) > cmplntv.log 2>&1

exem2s:
	@-$(CC) $(CC_FLAG) -m32 *src.c -o exem2s $(CC_INC) $(M2S_LIB) > cmplm2s.log 2>&1

runm2s:
	M2S_OPENCL_BINARY=./post_decrement_int2.bin $(M2S) --si-sim functional ./exem2s > runm2s.log 2>&1

runm2sisa:
	M2S_OPENCL_BINARY=./post_decrement_int2.bin $(M2S) --si-sim functional --si-debug-isa debug.isa ./exem2s > runm2s.log 2>&1

runntv:
	./exentv > runntv.log 2>&1

diff:
	diff exentv.result exem2s.result > check.log 2>&1

run: runm2s runntv diff
	echo "Diff: m2s vs native:" | cat check.log

clean:
	rm -rf exentv exem2s *.isa *.log *.bin *.result
