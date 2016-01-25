AMDAPPSDK_ROOT = /opt/AMDAPP/
M2S_ROOT = /home/xgong/multi2sim-4.2/
M2C_CC = $(M2S_ROOT)bin/m2c
M2S_LIB= -L $(M2S_ROOT)/lib/.libs -lm2s-opencl
AMD_CC = /home/xgong/multi2sim-4.2/bin/m2c
M2S = /home/xgong/multi2sim-4.2/bin/m2s

CC = gcc
CC_FLAG = -Werror -Wall -g -std=c99
CC_INC = -I $(AMDAPPSDK_ROOT)include/
CC_LIB = -L $(AMDAPPSDK_ROOT)lib/x86_64/ -lOpenCL
