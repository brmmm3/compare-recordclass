
import sys
import timeit
from dataclasses import dataclass

from collections import namedtuple
from recordclass import recordclass


@dataclass
class DCTest:
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int


NTTest = namedtuple('NTTest', 'a b c d e f')
RCTest = recordclass('RCTest', 'a b c d e f')

nttest = NTTest(1, 2, 3, 6, 5, 4)
rctest = RCTest(1, 2, 3, 6, 5, 4)
dctest = DCTest(1, 2, 3, 6, 5, 4)


def NTTestCreate():
    return NTTest(1, 2, 3, 6, 5, 4)

def RCTestCreate():
    return RCTest(1, 2, 3, 6, 5, 4)

def DCTestCreate():
    return DCTest(1, 2, 3, 6, 5, 4)


def NTTestSumIdx():
    return nttest[0] + nttest[1] + nttest[2] + nttest[3] + nttest[4] + nttest[5]

def RCTestSumIdx():
    return rctest[0] + rctest[1] + rctest[2] + rctest[3] + rctest[4] + rctest[5]


def NTTestSumName():
    return nttest.a + nttest.b + nttest.c + nttest.d + nttest.e + nttest.f

def RCTestSumName():
    return rctest.a + rctest.b + rctest.c + rctest.d + rctest.e + rctest.f

def DCTestSumName():
    return dctest.a + dctest.b + dctest.c + dctest.d + dctest.e + dctest.f


def NTTestSort():
    return sorted(nttest)

def RCTestSort():
    return sorted(rctest)

print('Object Size')
print(f'namedtuple: {sys.getsizeof(nttest)} bytes')
print(f'recordclass: {sys.getsizeof(rctest)} bytes')
print(f'dataclass: {sys.getsizeof(dctest)} bytes')

print('Create')
print(f'namedtuple: {timeit.timeit(NTTestCreate):.3f}')
print(f'recordclass: {timeit.timeit(RCTestCreate):.3f}')
print(f'dataclass: {timeit.timeit(DCTestCreate):.3f}')

print('Sum by index')
print(f'namedtuple: {timeit.timeit(NTTestSumIdx):.3f}')
print(f'recordclass: {timeit.timeit(RCTestSumIdx):.3f}')

print('Sum by name')
print(f'namedtuple: {timeit.timeit(NTTestSumName):.3f}')
print(f'recordclass: {timeit.timeit(RCTestSumName):.3f}')
print(f'dataclass: {timeit.timeit(DCTestSumName):.3f}')

print('Sort')
print(f'namedtuple: {timeit.timeit(NTTestSort):.3f}')
print(f'recordclass: {timeit.timeit(RCTestSort):.3f}')
