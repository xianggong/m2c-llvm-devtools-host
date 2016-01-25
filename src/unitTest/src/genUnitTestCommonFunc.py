#!/usr/bin/python

from unitTestFunc import unitTestFunc


# Genertic datatype
gentype = ["float", "float2", "float4", "float8", "float16"]

common_func_list = [[gentype, 3, gentype, gentype, gentype, "clamp"],
                    [gentype, 1, gentype, "degrees"],
                    [gentype, 2, gentype, gentype, "max"],
                    [gentype, 2, gentype, gentype, "min"],
                    [gentype, 3, gentype, gentype, gentype, "mix"],
                    [gentype, 1, gentype, "radians"],
                    [gentype, 2, gentype, gentype, "step"],
                    [gentype, 3, gentype, gentype, gentype, "smoothstep"],
                    [gentype, 1, gentype, "sign"]]


def main():

        for commonFunc in common_func_list:
                dstTypes = commonFunc[0]
                srcCount = commonFunc[1]
                commonFuncLiteral = commonFunc[2 + srcCount]
                for dataTypeIdx in range(len(dstTypes)):
                        dst = []
                        src = []
                        dst.append(dstTypes[dataTypeIdx])
                        for idx in range(srcCount):
                                srcTypes = commonFunc[2 + idx]
                                src.append(srcTypes[dataTypeIdx])
                        obj = unitTestFunc(src, dst, commonFuncLiteral)
                        obj.dumpAll("../test/common/")

if __name__ == "__main__":
        main()
