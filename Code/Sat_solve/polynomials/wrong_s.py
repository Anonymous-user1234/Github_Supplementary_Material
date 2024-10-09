import os
import random
import numpy as np

def evaluate_polynomial(polynomial, hasone_flag, sol_val):
    result = 0
    if hasone_flag:
        result += 1
    for i, term in enumerate(polynomial):
        flag = True
        for item in term:
            if item > 79:
                assert(0)
            if(sol_val[item] == 0):
                flag = False
                break
        if flag == True:
            result += 1
    return result

def read_polynomials_from_file(file_path): 

    f = open(file_path, 'r')
    all_lines = f.readlines()
    f.close()
    
    line_count = {}
    for line in all_lines:
        stp_line = line.strip()
        line_count[stp_line] = line_count.get(stp_line, 0) + 1
    
    uni_lines = [line for line in all_lines if line_count[line.strip()] % 2 == 1 ]

    with open(file_path, 'w') as file:
        file.writelines(uni_lines)


#########################################
directory = "polynomial-4"
#########################################

for filename in os.listdir(directory):
    # print("\n\n")
    file_path = os.path.join(directory, filename)
    # print("Processing file:", filename)
    read_polynomials_from_file(file_path)

    
