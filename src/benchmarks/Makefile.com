CC = /usr/bin/gcc44 
CXX = /usr/bin/g++44

M2S_LIB = /home/xgong/multi2sim-4.2/lib/.libs 
M2S_BIN = /home/xgong/multi2sim-4.2/bin/m2s 

INC = -I ../../../include -I ../../../include/SDKUtil
LD = -L $(M2S_LIB) -ldl -lrt -pthread -lm -l:libm2s-opencl.a

SI_CONFIG = /home/xgong/multi2sim-4.2/samples/southern-islands/7970/si-config
MEM_CONFIG = /home/xgong/multi2sim-4.2/samples/southern-islands/7970/mem-config
