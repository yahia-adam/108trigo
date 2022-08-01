#!/usr/bin/python3
from copy import deepcopy
import handling_matrix
from math import *

def exp(mx):
    final_mx = handling_matrix.identity_mx(mx)
    final_mx = handling_matrix.addition_mx(final_mx, mx)
    for i in range(2, 50):
        final_mx = handling_matrix.addition_mx(final_mx, handling_matrix.divide_mx(handling_matrix.power_mx(mx,i), factorial(i)))
    return final_mx

def cos(mx):
    final_mx = handling_matrix.identity_mx(mx)
    is_sub = True
    for i in range(2, 50, 2):
        if is_sub:
            final_mx = handling_matrix.substraction_mx(final_mx, handling_matrix.divide_mx(handling_matrix.power_mx(mx,i), factorial(i)))
        else:
            final_mx = handling_matrix.addition_mx(final_mx, handling_matrix.divide_mx(handling_matrix.power_mx(mx,i), factorial(i)))
        is_sub = not is_sub
    return final_mx

def sin(mx):
    final_mx = deepcopy(mx)
    is_sub = True
    for i in range(3, 50, 2):
        if is_sub:
            final_mx = handling_matrix.substraction_mx(final_mx, handling_matrix.divide_mx(handling_matrix.power_mx(mx,i), factorial(i)))
        else:
            final_mx = handling_matrix.addition_mx(final_mx, handling_matrix.divide_mx(handling_matrix.power_mx(mx,i), factorial(i)))
        is_sub = not is_sub
    return final_mx

def sinh(mx):
    return handling_matrix.divide_mx(handling_matrix.substraction_mx(exp(mx), exp(handling_matrix.multiplication_mx_scalar(mx, -1))), 2)

def cosh(mx):
    return handling_matrix.divide_mx(handling_matrix.addition_mx(exp(mx), exp(handling_matrix.multiplication_mx_scalar(mx, -1))), 2)
