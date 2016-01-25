#!/usr/bin/python


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def getInitValue(dataType, initVal):
        val = int(initVal)
        valf = float(initVal)
        initValDic = {"char": [val],
                      "char2": [val, val],
                      "char4": [val, val, val, val],
                      "char8": [val, val, val, val, val, val, val, val],
                      "char16": [val, val, val, val, val, val, val, val,
                                 val, val, val, val, val, val, val, val],
                      "uchar": [val],
                      "uchar2": [val, val],
                      "uchar4": [val, val, val, val],
                      "uchar8": [val, val, val, val, val, val, val, val],
                      "uchar16": [val, val, val, val, val, val, val, val,
                                  val, val, val, val, val, val, val, val],
                      "short": [val],
                      "short2": [val, val],
                      "short4": [val, val, val, val],
                      "short8": [val, val, val, val, val, val, val, val],
                      "short16": [val, val, val, val, val, val, val, val,
                                  val, val, val, val, val, val, val, val],
                      "ushort": [val],
                      "ushort2": [val, val],
                      "ushort4": [val, val, val, val],
                      "ushort8": [val, val, val, val, val, val, val, val],
                      "ushort16": [val, val, val, val, val, val, val, val,
                                   val, val, val, val, val, val, val, val],
                      "int": [val],
                      "int2": [val, val],
                      "int4": [val, val, val, val],
                      "int8": [val, val, val, val, val, val, val, val],
                      "int16": [val, val, val, val, val, val, val, val,
                                val, val, val, val, val, val, val, val],
                      "uint": [val],
                      "uint2": [val, val],
                      "uint4": [val, val, val, val],
                      "uint8": [val, val, val, val, val, val, val, val],
                      "uint16": [val, val, val, val, val, val, val, val,
                                 val, val, val, val, val, val, val, val],
                      "long": [val],
                      "long2": [val, val],
                      "long4": [val, val, val, val],
                      "long8": [val, val, val, val, val, val, val, val],
                      "long16": [val, val, val, val, val, val, val, val,
                                 val, val, val, val, val, val, val, val],
                      "ulong": [val],
                      "ulong2": [val, val],
                      "ulong4": [val, val, val, val],
                      "ulong8": [val, val, val, val, val, val, val, val],
                      "ulong16": [val, val, val, val, val, val, val, val,
                                  val, val, val, val, val, val, val, val],
                      "int": [val],
                      "int2": [val, val],
                      "int4": [val, val, val, val],
                      "int8": [val, val, val, val, val, val, val, val],
                      "int16": [val, val, val, val, val, val, val, val,
                                val, val, val, val, val, val, val, val],
                      "float": [valf],
                      "float2": [valf, valf],
                      "float4": [valf, valf, valf, valf],
                      "float8": [valf, valf, valf, valf,
                                 valf, valf, valf, valf],
                      "float16": [valf, valf, valf, valf,
                                  valf, valf, valf, valf,
                                  valf, valf, valf, valf,
                                  valf, valf, valf, valf]}

        dataTypeHost = str(initValDic[dataType])
        if hasNumbers(dataType):
                dataTypeHost = dataTypeHost.replace("[", "{{")
                dataTypeHost = dataTypeHost.replace("]", "}}")
        else:
                dataTypeHost = dataTypeHost.replace("[", "(")
                dataTypeHost = dataTypeHost.replace("]", ")")
        return dataTypeHost
