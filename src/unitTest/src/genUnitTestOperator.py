#!/usr/bin/python

from unitTestOperator import unitTestOperator


# Genertic datatype
gentype = ["char", "char2", "char4", "char8", "char16",
           "uchar", "uchar2", "uchar4", "uchar8", "uchar16",
           "short", "short2", "short4", "short8", "short16",
           "ushort", "ushort2", "ushort4", "ushort8", "ushort16",
           "int", "int2", "int4", "int8", "int16",
           "uint", "uint2", "uint4", "uint8", "uint16",
           "long", "long2", "long4", "long8", "long16",
           "ulong", "ulong2", "ulong4", "ulong8", "ulong16",
           "int", "int2", "int4", "int8", "int16",
           "float", "float2", "float4", "float8", "float16"]

rlttype = ["int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16",
           "int", "int2", "int4", "int8", "int16"]

divtype = ["float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16",
           "float", "float2", "float4", "float8", "float16"]

inttype = ["char", "char2", "char4", "char8", "char16",
           "uchar", "uchar2", "uchar4", "uchar8", "uchar16",
           "short", "short2", "short4", "short8", "short16",
           "ushort", "ushort2", "ushort4", "ushort8", "ushort16",
           "int", "int2", "int4", "int8", "int16",
           "uint", "uint2", "uint4", "uint8", "uint16",
           "long", "long2", "long4", "long8", "long16",
           "ulong", "ulong2", "ulong4", "ulong8", "ulong16",
           "int", "int2", "int4", "int8", "int16"]

btwtype = []

lgctype = []

sfttype = []

operator_list = [
                [gentype, 2, gentype, gentype, "+", "add", "s0-op-s1"],
                [gentype, 2, gentype, gentype, "-", "subtract", "s0-op-s1"],
                [gentype, 2, gentype, gentype, "*", "multiply", "s0-op-s1"],
                [divtype, 2, gentype, gentype, "/", "divide", "s0-op-s1"],
                [inttype, 2, inttype, inttype, "%", "remainder", "s0-op-s1"],
                [gentype, 1, gentype,          "+", "unary_plus", "op-s0"],
                [gentype, 1, gentype,          "-", "unary_minus", "op-s0"],
                [gentype, 1, gentype,          "++", "post_increment", "s0-op"],
                [gentype, 1, gentype,          "++", "pre_increment", "op-s0"],
                [gentype, 1, gentype,          "--", "post_decrement", "s0-op"],
                [gentype, 1, gentype,          "--", "pre_decrement", "op-s0"],
                [rlttype, 2, gentype, gentype, ">", "relational_greater_than", "s0-op-s1"],
                [rlttype, 2, gentype, gentype, "<", "relational_less_than", "s0-op-s1"],
                [rlttype, 2, gentype, gentype, ">=", "relational_greater_than_or_equal_to", "s0-op-s1"],
                [rlttype, 2, gentype, gentype, "<=", "relational_less_than_or_equal_to", "s0-op-s1"],
                [rlttype, 2, gentype, gentype, "==", "equal", "s0-op-s1"],
                [rlttype, 2, gentype, gentype, "!=", "not_equal", "s0-op-s1"],
                # [btwtype, 2, gentype, gentype, "&", "bitwise_and", "s0-op-s1"],
                # [btwtype, 2, gentype, gentype, "|", "bitwise_or", "s0-op-s1"],
                # [btwtype, 2, gentype, gentype, "^", "bitwise_not", "s0-op-s1"],
                # [btwtype, 2, gentype, gentype, "~", "bitwise_not", "s0-op-s1"],
                # [lgctype, 2, gentype, gentype, "&&", "logical_and", "s0-op-s1"],
                # [lgctype, 2, gentype, gentype, "||", "logical_or", "s0-op-s1"],
                # [lgctype, 2, gentype, gentype, "^^", "logical_exclusive_or", "s0-op-s1"],
                # [lgctype, 2, gentype, gentype, "!", "logical_unary_not", "s0-op-s1"],
                # [sfttype, 2, gentype, gentype, ">>", "right_shift", "s0-op-s1"],
                # [sfttype, 2, gentype, gentype, "<<", "left_shift", "s0-op-s1"]
                ]


def main():

        for operator in operator_list:
                dstTypes = operator[0]
                srcCount = operator[1]
                operatorLiteral = operator[2 + srcCount]
                operatorName = operator[3 + srcCount]
                operatorUsage = operator[4 + srcCount]
                for dataTypeIdx in range(len(dstTypes)):
                        dst = []
                        src = []
                        dst.append(dstTypes[dataTypeIdx])
                        for idx in range(srcCount):
                                srcTypes = operator[2 + idx]
                                src.append(srcTypes[dataTypeIdx])
                        obj = unitTestOperator(src, dst, operatorLiteral,
                                           operatorName, operatorUsage)
                        obj.dumpAll("../test/operator/")

if __name__ == "__main__":
        main()
