import os
import mpmath as mp
from mpmath import *


def Clear():
    os.system('cls')


def Bernoulli():
    global seq, sig, k

    mp.dps = sig

    while True:

        seq.append(1/mp.factorial(k))
        print(f'\n{k + 1}: {mpf(sum(seq))}')

        if mpf(sum(seq)) == mpf(sum(seq)) - seq[k]:
            break
        else:
            Clear()
            k = k + 1
            continue

    print('\nEnd')


def Menu():
    global sig

    Clear()

    sig = int(input('Number of significant algharisms: '))

    while sig <= 0:

        print('\nImpossible number\n')
        sig = int(input('Try Again: '))
    else:
        Bernoulli()


seq = []
k = 0
sig = 0

Menu()
