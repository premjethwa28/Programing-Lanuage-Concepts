# Name - Prem Atul Jethwa
# Student Id - 1001861810
# NetID - paj1810
# Date of submission - 04/04/2023
# OS - Mac
# Language Version - Python 3.6.2

# Extra operator used are ‘%’ and ‘^’
# Please refer paj1810_Lab03_readme.pdf file for steps to run Lab 03.

import os


def operator_priority_check(sign):
    # Key : Value pairing and setting there priority
    operator = {'+': (1), '-': (1), '*': (2), '/': (2), '%': (2), '^': (4)}
    if sign in operator.keys():
        return 1
    else:
        return 0


file_uploaded = open(os.path.join(
    os.getcwd(), 'input_RPN_EC.txt'), encoding='utf-8')
for i in file_uploaded:
    expres = i
    expres_split = expres.split()
    st_op_li = []
    rpn_exeption = []
    # Key : Value paring and setting there priority
    operator = {'+': (1), '-': (1), '*': (2), '/': (2), '%': (2), '^': (4)}
    for m in expres_split:
        # Check if it opening parenthesis
        if m == '(':
            st_op_li.append(m)
        elif m == ')':                                                      # Check if it closing parenthesis
            # Runs untill it does not come accross "("
            while st_op_li and st_op_li[-1] != '(':
                rpn_exeption.append(st_op_li.pop())
            st_op_li.pop()
        elif operator_priority_check(m):
            while st_op_li and operator_priority_check(st_op_li[-1]):
                if operator[m]-operator[st_op_li[-1]] < 0:
                    rpn_exeption.append(st_op_li.pop())
                    continue
                break
            # The incoming operator is placed at the top of the stack if the operator stack is empty or if it has a higher priority than the top of the stack.
            st_op_li.append(m)
        else:
            rpn_exeption.append(m)
    while st_op_li:
        rpn_exeption.append(st_op_li.pop())
    final_result = []
    for j in rpn_exeption:  # Check if it is a operator
        if operator_priority_check(j):
            # Pop number j is operator
            digit1 = int(final_result.pop())
            digit2 = int(final_result.pop())
            # Filtering type of operations and performing the calculations.
            if j == '+':
                j = digit1+digit2
            elif j == '-':
                j = digit2-digit1
            elif j == '*':
                j = digit1*digit2
            elif j == '/':
                j = digit2/digit1
            elif j == '%':  # Extra operation that are added in this code
                j = digit2 % digit1
            elif j == '^':  # Extra operation that are added in this code
                j = pow(digit2, digit1)
            # After performing the operations add the answer to the stack again
            final_result.append(j)
        else:
            final_result.append(j)
    print("RPN Expression is:", rpn_exeption)
    print("RPN value is: ", int(final_result[0]))
# Closing the open file
file_uploaded.close()
