# -*- coding: utf-8 -*
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

1. 暴力递归求解法
问题是会有大量重复计算问题 因为左边fib(N - 1) 肯定是计算过fib(N - 2), fib(N - 2)右侧又计算一遍 
"""
def fib(N):
  if N == 0 or N == 1:
      return N
  if N > 1:
    return fib(N - 1) + fib(N - 2)