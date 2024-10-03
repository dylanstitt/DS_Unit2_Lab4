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
    solution = [[] for i in range(len(m1))]

    if len(m1[0]) == len(m2):
        m2 = [[i[j] for i in m2] for j in range(len(m2[0]))]
        for row in range(len(m1)):
            for col in range(len(m2)):
                num = sum([m1[row][i]*m2[col][i] for i in range(len(m1[row]))])
                solution[row].append(num)

    return solution

def display(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

def main():
    AB = matMul(A, B)
    CD = matMul(C, D)

    display(AB)
    print('\n')
    display(CD)


if __name__ == '__main__':
    main()