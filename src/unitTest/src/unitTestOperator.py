#!/usr/bin/python

from unitTest import unitTest


class unitTestOperator(unitTest):
        """docstring for unitTestOperator"""
        def __init__(self,
                     srcTypes, dstType,
                     operator, operatorName,
                     usage):
                super(unitTestOperator, self).__init__(operatorName,
                                                       srcTypes,
                                                       dstType)
                self.operator = operator
                self.operatorName = operatorName
                self.usage = usage.split("-")
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

                for elem in self.usage:
                        if elem == "s0":
                                main += " src_0[gid] "
                        elif elem == "op":
                                main += self.operator
                        elif elem == "s1":
                                main += " src_1[gid]"

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
