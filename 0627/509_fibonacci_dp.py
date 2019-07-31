# -*- coding: utf-8 -*

"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

递归方法有个问题是, 会产生多余的信息, 而且有些信息我们是重复解答的
DP: Dynamic Programming

计算机解决问题其实没有任何奇技淫巧，它唯一的解决办法就是穷举，穷举所有可能性。
算法设计无非就是先思考 “如何穷举”，然后再追求 “如何聪明地穷举”。
"""
def fib(N):
  if N == 0 or N == 1: return N
  # fib(N) = fib(N - 1) + fib(N - 2), 只需要知道 从 2 到 N - 1的问题即可
  _dict = {
    0: 0,
    1: 1
  }
  i = 2
  while i < N:
    _dict[i] = _dict[i - 1] + _dict[i - 2]
    i += 1

  print(_dict)
  return _dict[N - 1] + _dict[N - 2]

print(fib(6))

def fib(N):
  if N < 2: return N

  F = [0, 1]
  i = 2
  # 例如 N = 6, 那就是 到5这个数位置 (5) + (4)的问题
  while i < N:
    F.append(F[i - 1] + F[i - 2])
    i += 1
  return F[i - 1] + F[i - 2]

print(fib(6))