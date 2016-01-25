#!/usr/bin/python

from unitTestFunc import unitTestFunc


gentype = ["float", "float2", "float4", "float8", "float16"]
inttype = ["int", "int2", "int4", "int8", "int16"]

math_func_list = [[gentype, 1, gentype, "acos"],
                  [gentype, 1, gentype, "acosh"],
                  [gentype, 1, gentype, "acospi"],
                  [gentype, 1, gentype, "asin"],
                  [gentype, 1, gentype, "asinh"],
                  [gentype, 1, gentype, "asinpi"],
                  [gentype, 1, gentype, "atan"],
                  [gentype, 2, gentype, gentype, "atan2"],
                  [gentype, 1, gentype, "atanh"],
                  [gentype, 1, gentype, "atanpi"],
                  [gentype, 2, gentype, gentype, "atan2pi"],
                  [gentype, 1, gentype, "cbrt"],
                  [gentype, 1, gentype, "ceil"],
                  [gentype, 2, gentype, gentype, "copysign"],
                  [gentype, 1, gentype, "cos"],
                  [gentype, 1, gentype, "cosh"],
                  [gentype, 1, gentype, "cospi"],
                  [gentype, 1, gentype, "erfc"],
                  [gentype, 1, gentype, "erf"],
                  [gentype, 1, gentype, "exp"],
                  [gentype, 1, gentype, "exp2"],
                  [gentype, 1, gentype, "exp10"],
                  [gentype, 1, gentype, "expm1"],
                  [gentype, 1, gentype, "fabs"],
                  [gentype, 2, gentype, gentype, "fdim"],
                  [gentype, 1, gentype, "floor"],
                  [gentype, 3, gentype, gentype, gentype, "fma"],
                  [gentype, 2, gentype, gentype, "fmax"],
                  [gentype, 1, gentype, "fmin"],
                  [gentype, 2, gentype, gentype, "fmod"],
                  # [gentype, 1, gentype, "fract"],
                  # [gentype, 1, gentype, "frexp"],
                  [gentype, 2, gentype, gentype, "hypot"],
                  [gentype, 1, gentype, "ilogb"],
                  [gentype, 1, gentype, "ldexp"],
                  [gentype, 1, gentype, "lgamma"],
                  # [gentype, 1, gentype, "lgamma_r"],
                  [gentype, 1, gentype, "log"],
                  [gentype, 1, gentype, "log10"],
                  [gentype, 1, gentype, "log1p"],
                  [gentype, 1, gentype, "logb"],
                  [gentype, 3, gentype, gentype, gentype, "mad"],
                  # [gentype, 1, gentype, "modf"],
                  # [gentype, 1, "uint", nan"],
                  [gentype, 2, gentype, gentype, "nextafter"],
                  [gentype, 2, gentype, gentype, "pow"],
                  [gentype, 2, gentype, inttype, "pown"],
                  [gentype, 2, gentype, gentype, "powr"],
                  [gentype, 2, gentype, gentype, "remainder"],
                  # [gentype, 1, gentype, gentype, , "remquo"],
                  [gentype, 1, gentype, "rint"],
                  [gentype, 2, gentype, inttype, "rootn"],
                  [gentype, 1, gentype, "round"],
                  [gentype, 1, gentype, "rsqrt"],
                  [gentype, 1, gentype, "sin"],
                  # [gentype, 1, gentype, , "sincos"],
                  [gentype, 1, gentype, "sinh"],
                  [gentype, 1, gentype, "sinpi"],
                  [gentype, 1, gentype, "sqrt"],
                  [gentype, 1, gentype, "tan"],
                  [gentype, 1, gentype, "tanh"],
                  [gentype, 1, gentype, "tanpi"],
                  [gentype, 1, gentype, "tgamma"],
                  [gentype, 1, gentype, "trunc"],
                  [gentype, 1, gentype, "half_cos"],
                  [gentype, 2, gentype, gentype, "half_divide"],
                  [gentype, 1, gentype, "half_exp"],
                  [gentype, 1, gentype, "half_exp2"],
                  [gentype, 1, gentype, "half_exp10"],
                  [gentype, 1, gentype, "half_log"],
                  [gentype, 1, gentype, "half_log2"],
                  [gentype, 1, gentype, "half_log10"],
                  [gentype, 2, gentype, gentype, "half_powr"],
                  [gentype, 1, gentype, "half_recip"],
                  [gentype, 1, gentype, "half_rsqrt"],
                  [gentype, 1, gentype, "half_sin"],
                  [gentype, 1, gentype, "half_sqrt"],
                  [gentype, 1, gentype, "half_tan"],
                  [gentype, 1, gentype, "native_cos"],
                  [gentype, 1, gentype, "native_divide"],
                  [gentype, 1, gentype, "native_exp"],
                  [gentype, 1, gentype, "native_exp2"],
                  [gentype, 1, gentype, "native_exp10"],
                  [gentype, 1, gentype, "native_log"],
                  [gentype, 1, gentype, "native_log2"],
                  [gentype, 1, gentype, "native_log10"],
                  [gentype, 1, gentype, "native_powr"],
                  [gentype, 1, gentype, "native_recip"],
                  [gentype, 1, gentype, "native_rsqrt"],
                  [gentype, 1, gentype, "native_sin"],
                  [gentype, 1, gentype, "native_sqrt"],
                  [gentype, 1, gentype, "native_tan"]]


def main():
        for mathFinc in math_func_list:
                dstTypes = mathFinc[0]
                srcCount = mathFinc[1]
                mathFincLiteral = mathFinc[2 + srcCount]
                for dataTypeIdx in range(len(dstTypes)):
                        dst = []
                        src = []
                        dst.append(dstTypes[dataTypeIdx])
                        for idx in range(srcCount):
                                srcTypes = mathFinc[2 + idx]
                                src.append(srcTypes[dataTypeIdx])
                        obj = unitTestFunc(src, dst, mathFincLiteral)
                        obj.dumpAll("../test/math/")

if __name__ == "__main__":
        main()
