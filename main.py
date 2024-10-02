# Dylan Stitt
# Unit 2 Lab 4
# Matrices

from samples import *
from testcode import *

def matAdd(m1, m2):
    solution = [[] for i in range(len(m1))]

    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
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