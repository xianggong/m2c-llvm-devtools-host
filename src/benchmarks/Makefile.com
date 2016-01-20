CC = gcc
CXX = g++

M2S_LIB = /home/xgong/multi2sim-4.2/lib/.libs 
M2S_BIN = /home/xgong/multi2sim-4.2/bin/m2s 

INC = -I ../../../include -I ../../../include/SDKUtil
LD = -L $(M2S_LIB) -ldl -lrt -pthread -l:libm2s-opencl.a -l:libm.a
