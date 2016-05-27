AMDAPPSDK_ROOT = /opt/AMDAPP/
M2S_ROOT = /home/xgong/m2s50/multi2sim
M2C_CC = /home/xgong/Develop/multi2sim/bin/m2c
M2S_LIB= $(M2S_ROOT)/lib/.libs
AMD_CC = /home/xgong/Develop/multi2sim/bin/m2c
M2S = /home/xgong/m2s50/multi2sim/bin/m2s

CC = gcc
CC_FLAG = -Werror -Wall -g -std=c99
CC_INC = -I $(AMDAPPSDK_ROOT)include/
CC_LIB = -L $(AMDAPPSDK_ROOT)lib/x86_64/ -lOpenCL
