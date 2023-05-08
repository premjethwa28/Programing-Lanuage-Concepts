# Name - Prem Atul Jethwa
# Student Id - 1001861810
# NetID - paj1810
# Date of submission - 04/04/2023
# OS - Mac
# Language Version - Python 3.6.2

# Please refer paj1810_Lab03_readme.pdf file for steps to run Lab 03.

import os
# It only accepts 4 operators “+”, “-“, “*”, “/""
operators = ['+', '-', '*', '/']
# Opening and scanning the file line by line
file_uploaded = open(os.path.join(
    os.getcwd(), 'input_RPN.txt'), encoding='utf-8')
for i in file_uploaded:
    expression = i.split()                      # String separation
    stack_list = []
    for o in expression:
        if o in operators:                      # Check if it is a operator
            a = int(stack_list.pop())           # Pop number c is operator
            b = int(stack_list.pop())
            # Filtering type of operations and performing the calculations.
            if o == '+':
                answer = a+b
            elif o == '-':
                answer = b-a
            elif o == '*':
                answer = a*b
            elif o == '/':
                answer = b/a
            # After performing the operations add the answer to the stack again
            stack_list.append(answer)
        else:
            stack_list.append(o)
    print("Expression is:", expression)
    print("Answer:", int(stack_list[0]))
file_uploaded.close()                            # Closing the open file
