#!/usr/bin/python

from unitTestFunc import unitTestFunc


# Genertic datatype
gentype = ["char", "char2", "char4", "char8", "char16",
           "uchar", "uchar2", "uchar4", "uchar8", "uchar16",
           "short", "short2", "short4", "short8", "short16",
           "ushort", "ushort2", "ushort4", "ushort8", "ushort16",
           "int", "int2", "int4", "int8", "int16",
           "uint", "uint2", "uint4", "uint8", "uint16",
           "long", "long2", "long4", "long8", "long16",
           "ulong", "ulong2", "ulong4", "ulong8", "ulong16"]

# Unsigned genertic datatype
ugentype = ["uchar", "uchar2", "uchar4", "uchar8", "uchar16",
            "uchar", "uchar2", "uchar4", "uchar8", "uchar16",
            "ushort", "ushort2", "ushort4", "ushort8", "ushort16",
            "ushort", "ushort2", "ushort4", "ushort8", "ushort16",
            "uint", "uint2", "uint4", "uint8", "uint16",
            "uint", "uint2", "uint4", "uint8", "uint16",
            "ulong", "ulong2", "ulong4", "ulong8", "ulong16",
            "ulong", "ulong2", "ulong4", "ulong8", "ulong16"]

integer_func_list = [[ugentype, 1, gentype, "abs"],
                    [ugentype, 2, gentype, gentype, "abs_diff"],
                    [gentype, 2, gentype, gentype, "add_sat"],
                    [gentype, 2, gentype, gentype, "hadd"],
                    [gentype, 2, gentype, gentype, "rhadd"],
                    [gentype, 1, gentype, "clz"],
                    [gentype, 3, gentype, gentype, gentype, "mad_hi"],
                    [gentype, 3, gentype, gentype, gentype, "mad_sat"],
                    [gentype, 2, gentype, gentype, "max"],
                    [gentype, 2, gentype, gentype, "min"],
                    [gentype, 2, gentype, gentype, "mul_hi"],
                    [gentype, 2, gentype, gentype, "rotate"],
                    [gentype, 2, gentype, gentype, "sub_sat"]]


def main():
        for integerFinc in integer_func_list:
                dstTypes = integerFinc[0]
                srcCount = integerFinc[1]
                integerFincLiteral = integerFinc[2 + srcCount]
                for dataTypeIdx in range(len(dstTypes)):
                        dst = []
                        src = []
                        dst.append(dstTypes[dataTypeIdx])
                        for idx in range(srcCount):
                                srcTypes = integerFinc[2 + idx]
                                src.append(srcTypes[dataTypeIdx])
                        obj = unitTestFunc(src, dst, integerFincLiteral)
                        obj.dumpAll("../test/integer/")

if __name__ == "__main__":
        main()
