#!/usr/bin/python

from unitTestFunc import unitTestFunc


floattype = ["float", "float2", "float4", "float8", "float16"]
inttype = ["int", "int2", "int4", "int8", "int16"]

gentype = ["char", "char2", "char4", "char8", "char16",
           "uchar", "uchar2", "uchar4", "uchar8", "uchar16",
           "short", "short2", "short4", "short8", "short16",
           "ushort", "ushort2", "ushort4", "ushort8", "ushort16",
           "int", "int2", "int4", "int8", "int16",
           "uint", "uint2", "uint4", "uint8", "uint16",
           "long", "long2", "long4", "long8", "long16",
           "ulong", "ulong2", "ulong4", "ulong8", "ulong16"]

relational_func_list = [[inttype, 2, floattype, floattype, "isequal"],
                        [inttype, 2, floattype, floattype, "isnotequal"],
                        [inttype, 2, floattype, floattype, "isgreater"],
                        [inttype, 2, floattype, floattype, "isgreaterequal"],
                        [inttype, 2, floattype, floattype, "isless"],
                        [inttype, 2, floattype, floattype, "islessequal"],
                        [inttype, 2, floattype, floattype, "islessgreater"],
                        [inttype, 1, floattype, "isfinite"],
                        [inttype, 1, floattype, "isinf"],
                        [inttype, 1, floattype, "isnan"],
                        [inttype, 1, floattype, "isnormal"],
                        [inttype, 2, floattype, floattype, "isordered"],
                        [inttype, 2, floattype, floattype, "isunordered"],
                        [inttype, 1, floattype, "signbit"],
                        # [["int"], 2, igentype, "any"],
                        # [["int"], 2, igentype, "all"],
                        [gentype, 3, gentype, gentype, gentype, "bitselect"]
                        # [gentype, 2, gentype, gentype, igentype, "select"]
                        # [gentype, 2, gentype, gentype, ugentype, "select"]
                        ]


def main():
        for relationalFunc in relational_func_list:
                dstTypes = relationalFunc[0]
                srcCount = relationalFunc[1]
                relationalFuncLiteral = relationalFunc[2 + srcCount]
                for dataTypeIdx in range(len(dstTypes)):
                        dst = []
                        src = []
                        dst.append(dstTypes[dataTypeIdx])
                        for idx in range(srcCount):
                                srcTypes = relationalFunc[2 + idx]
                                src.append(srcTypes[dataTypeIdx])
                        obj = unitTestFunc(src, dst, relationalFuncLiteral)
                        obj.dumpAll("../test/relational/")

if __name__ == "__main__":
        main()
