#!/usr/bin/python

from unitTest import unitTest


class unitTestFunc(unitTest):
        """ Base class for unit test of build-in functions """
        def __init__(self, srcTypes, dstType, funcName):
                super(unitTestFunc, self).__init__(funcName,
                                                   srcTypes,
                                                   dstType)
                self.funcName = funcName
                # Check if explicit casting is needed
                if srcTypes[0] == dstType[0]:
                        self.isCastNeeded = False
                else:
                        self.isCastNeeded = True

        def getKernelSrcMain(self):
                main = ""
                # Append cast if needed
                if self.isCastNeeded:
                        main += "(" + self.dstType[0] + ")("

                main += self.funcName + "("

                for srcIdx in range(len(self.srcTypes)):
                        main += "src_" + str(srcIdx) + "[gid]"
                        if srcIdx != len(self.srcTypes) - 1:
                                main += ", "
                main += ")"

                # Append cast if needed
                if self.isCastNeeded:
                        main += ");\n"
                else:
                        main += ";\n"

                return main

        def getKernelSrc(self):
                self.kernelSrc += self.getKernelSrcPrefix()
                self.kernelSrc += self.getKernelSrcMain()
                self.kernelSrc += self.getKernelSrcPostfix()
                return self.kernelSrc
