#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    new_grade = []
    
    for grade in grades:
        if grade < 38:
            new_grade.append(grade)
        else:
            multiple_of_five = math.ceil(grade / 5) * 5
            if multiple_of_five - grade < 3:
                new_grade.append(multiple_of_five)
            else:
                new_grade.append(grade)  
    
    return new_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
