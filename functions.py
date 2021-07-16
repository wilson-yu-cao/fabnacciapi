# Fibonacci number
def F(n):
  assert n>=0, 'assert n>=0'

  if n == 0:
    seq = [0]
  elif n == 1:
    seq = [0,1]
  elif n > 1 :
    seq = [0,1]
    for i in range(2, n+1):
      seq.append(seq[i-2] + seq[i-1])

  return seq