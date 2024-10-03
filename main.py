# Dylan Stitt
# Unit 2 Lab 4
# Matrices

from samples import *
from testcode import *

def mat_sum(m1, m2):
    solution = [[] for i in range(len(m1))]

    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            for j, k in enumerate(m1[i]):
                solution[i].append(k + m2[i][j])
        return solution

    return 'no solution'

def mat_mul(m1, m2):
    solution = [[] for i in range(len(m1))]

    if len(m1[0]) == len(m2):
        m2 = [[i[j] for i in m2] for j in range(len(m2[0]))]
        for row in range(len(m1)):
            for col in range(len(m2)):
                num = sum([m1[row][i] * m2[col][i] for i in range(len(m1[row]))])
                solution[row].append(num)
        return solution

    return 'no solution'

def main():
    # TEST 1 - valid matrix addition
    TEST_valid_mat_add()

    # TEST 2 - invalid matrix addition
    TEST_invalid_mat_add()

    # TEST 3 - Valid matrix multiplication
    # Mini Test 3.1 - One row, one column
    TEST_matmul_3_1()

    # Mini Test 3.2 - Two rows, one column
    TEST_matmul_3_2()

    # Mini Test 3.3 - Three rows, one column
    TEST_matmul_3_3()

    # Mini Test 3.4 - One row, two columns
    TEST_matmul_3_4()

    # Mini Test 3.5 - One row, three columns
    TEST_matmul_3_5()

    # Mini Test 3.6 - Many rows, many columns
    TEST_valid_mat_mul()

    #TEST 4 - Invalid matrix multiplication
    TEST_invalid_mat_mul()


if __name__ == '__main__':
    main()