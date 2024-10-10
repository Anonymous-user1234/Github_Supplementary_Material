# Github_Supplementary_Material

## Requirments (tested on Ubuntu 20.04):
1. Sage 10.3: https://www.sagemath.org
2. Singular 4.4.0: https://www.singular.uni-kl.de/index.php/singular-download/109.html
3. python-sat 1.8.dev13:
>pip3 install python-sat \
pip3 install pycryptosat==5.11.21



## Files:

### ./Data_spolys
The polynomials were obtained in the Offline Phase of the practical attack.

### ./Sat_solve

+ ***solve.py***: Python implementation of Algorithm 4("Solving the system constructed by the superpolys by testing").
+ ***line285***: Generate a secret key by random
+ ***line289***: Use a preset key (Hexadecimal)
+ ***Output Information (on-screen)***:
+ ***"round 2"***: The index of the iteration.
+ ***"untested vars"***: The list of indices of the untested secret variables, sorted by the increasing order of the appearing times.
+ ***"to test var"***: The index of the variable to be tested.
+ ***"current_assigns"***: The list of the assignments determined in previous iterations. Specifically, [[59], [-62]] means k59=1 and k62=0, which obtains from previous tests.
+ ***"both_has_solutions"***: The list of indices of variables whose values cannot be determined.
+ ***"testing k62 == 0"***: Testing whether k62 == 0 leads to a contradiction.
+ ***"cnf:  [[59], [60], [-62]] "***: Assigning {k59 == 1, k60 == 1, k62 = 0}.
+ ***"Find solution~~~"***: Found a soltuion by assigning {k59 == 1, k60 == 1, k62 = 0}.
+ ***"testing k62 == 1"***: Testing whether k62 == 1 leads to a contradiction.
+ ***"cnf:  [[59], [60], [62]] "***: Assigning {k59 == 1, k60 == 1, k62 = 1}.
+ ***"No solution!"***: Found a contradiciton by assigning {k59 == 1, k60 == 1, k62 = 1}, which implies k62 == 0 must hold.

---------------------------------------
...
2024-10-08 04:36:19.673821
round 2 \
untested vars:  [10, 8, 23, 6, 11, 21, 19, 9, 24, 7, 36, 5, 4, 12, 67, 42, 34, 32, 66, 80, 17, 31, 14, 51, 16, 41, 38, 15, 40, 39, 18, 55, 44, 2, 53, 1, 50, 76, 30, 56, 70, 3, 54, 13, 22, 29, 78, 57, 49, 68, 65, 20, 25, 43, 71, 52, 72, 28, 77, 74, 79, 27, 69, 46, 48, 73, 37, 26, 33, 64, 35, 47, 58, 45, 63, 75, 61] \
to test var: 62\
current_assigns:  [[59], [60]] 2 \
both_has_solutions:  [] 0\
testing k62 == 0\
cnf:  [[59], [60], [-62]] 

Find solution~~~

testing k62 == 1\
cnf:  [[59], [60], [62]]

No solution!

round is done

2024-10-08 04:42:57.665555\
round 3
...
------------------------------

+ ***polynomials***:  A folder storing a series of polynomial sets.

### ./GroebnerBasis_solve

+ ***GB_sage***: Solving equations by the Groebner basis method in Sage
+ ***gb.py***: The script for computing the Groebner basis (by Polybori) in Sage:
+ ***line48~50***: Choose the secret key.
+ ***logs***: Some logs show that the Groebner basis method fails to solve the whole system directly. Related keys are at the top of the logs.

+ ***GB_Singular***
+ ***singular_cmds***: Files containing the Singular commands generated by the "generate_singular_cmd.py" script.
+ ***logs***: Some logs show that the Groebner basis method fails to solve the whole system directly. Related keys are at the top of the logs.
+ ***generate_singular_cmd.py***: Generate Singular commands that can be executed on Singular:
+ ***line87~89***: Choose the secret key.

### ./Statistics_spolys

+ ***sp_degree.py***: Statistics of the degrees of the polynomials.
+ ***sp_monomial.py***: Statistics of the monomial numbers of the polynomials.
+ ***vars_frequency_832.py***: Statistics of the appearing times of the secret variables.


