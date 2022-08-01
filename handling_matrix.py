#!/usr/bin/python3
from copy import deepcopy

def create_mx(n):
    mx = list()
    for i in range(n):
        mx.append(list())
        for j in range(n):
            mx[i].append(0)
    return mx

def identity_mx(mx):
    n = len(mx)
    identity = create_mx(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                identity[i][j] = 1

    return identity

def addition_mx(mx1, mx2):
    n = len(mx1)
    final_mx = create_mx(n)
    for i in range(n):
        for j in range(n):
            final_mx[i][j] = mx1[i][j] + mx2[i][j]
    return final_mx

def substraction_mx(mx1, mx2):
    n = len(mx1)
    final_mx = create_mx(n)
    for i in range(n):
        for j in range(n):
            final_mx[i][j] = mx1[i][j] - mx2[i][j]
    return final_mx

def multiplication_mx(mx1, mx2):
    n = len(mx1)
    final_mx = create_mx(n)
    for i in range(n):
        for j in range(n):
            final_mx[i][j] = sum([ mx1[i][x]*mx2[x][j] for x in range(n)])
    return final_mx

def multiplication_mx_scalar(mx1, k):
    n = len(mx1)
    final_mx = create_mx(n)
    for i in range(n):
        for j in range(n):
            final_mx[i][j] = mx1[i][j] * k
    return final_mx

def divide_mx(mx1, k):
    n = len(mx1)
    final_mx = create_mx(n)
    for i in range(n):
        for j in range(n):
            final_mx[i][j] = mx1[i][j] / k
    return final_mx

def power_mx(mx, k):
    final_mx = deepcopy(mx)
    for i in range(2, k+1):
        final_mx = multiplication_mx(final_mx, mx)
    return final_mx
