import os
import random

def read_polynomials(folder):
    equations = {}
    used_vars = {}

    for filename in os.listdir(folder):
        file = open(os.path.join(folder, filename), "r")

        terms = []
        first_line_empty = False
        vars = set()
        for line in file:
            line = line.strip()
            if not terms and line == "":
                first_line_empty = True
            elif line:
                vars_in_line = [int(x) + 1 for x in line.split()]
                terms.append(vars_in_line)
                vars.update(vars_in_line)
        equations[filename] = (terms, first_line_empty)

        file.close()

        for ele in vars:
            if ele in used_vars:
                used_vars[ele] += 1
            else:
                used_vars[ele] = 1

    return equations, used_vars


def balance_test(equ):
    def evaluate_term(term, model):
        return all(model[var]for var in term)

    used_vars = [0 for _ in range(81)]
    for term in equ:
        for it in term:
            used_vars[it] += 1
    com_mon = []
    for i in range(81):
        if used_vars[i] == len(equ):
            com_mon += [i]

    test_num = 10000
    be1 = 0
    for _ in range(test_num):
        random_solution = [random.choice([i + 1, -(i + 1)]) for i in range(80)]
        # print(random_solution)
        model = {abs(lit): (lit > 0) for lit in random_solution}
        # print(model)
        lhs = 0
        for term in equ:
            # print(term, evaluate_term(term, model))
            lhs ^= evaluate_term(term, model)
        be1 += lhs

    if be1 > test_num / 2:
        be1 = test_num - be1

    return be1 * 1. / test_num, com_mon





if __name__ == "__main__":

    idx = 4

    equations, used_vars = read_polynomials(f"polynomials/polynomial-{idx}")

    tosort = []

    i = 0
    for filename, (terms, first_line_empty) in equations.items():

        bb, bc = balance_test(terms)

        tosort += [[bb, bc, filename]]
        print(i, " : ", filename, " : " , bb, bc)
        i += 1

        print(bb)


    print(tosort)
    tosort.sort()

    for it in tosort:
        print(it)






