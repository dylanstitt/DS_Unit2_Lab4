# Dylan Stitt
# Unit 2 Lab 4
# Matrices

from samples import *
from testcode import *

def matAdd(m1, m2):
    m1Dimensions = (len(m1), len(m1[0]))
    m2Dimensions = (len(m2), len(m2[0]))
    solution = [[] for i in range(m1Dimensions[0])]

    if m1Dimensions[0] == m2Dimensions[0] and m1Dimensions[1] == m2Dimensions[1]:
        for i in range(m1Dimensions[0]):
            for j, k in enumerate(m1[i]):
                solution[i].append(k + m2[i][j])

    return solution

def matMul(m1, m2):
    ...


def main():
    AplusB = matAdd(A, B)
    CplusD = matAdd(C, D)

    for i in [AplusB, CplusD]:
        for matrix in i:
            for j in matrix:
                print(j, end='  ')
            print()
        print('\n\n')


if __name__ == '__main__':
    main()