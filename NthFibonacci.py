""""
'Nth Fibonacci'
print('-'*30)
print('Nth Fibonacci')
print('-'*15)
getNthFib1 = 0
getNthFib2 = 1
n = int(input('n: '))
print('-'*30)
print(' {}, {}' .format(getNthFib1, getNthFib2), end='')
getNthFib3 = getNthFib1 + getNthFib2
print(', {}' .format(getNthFib3), end='')
cont = 3
while cont <= n:
    getNthFib3 = getNthFib1 + getNthFib2
    print(', {}' .format(getNthFib3), end='')
    getNthFib1 = getNthFib2
    getNthFib2 = getNthFib3
    cont +=1
 """

"""""
print('-'*15)
n = int(input('n: '))
print('-'*15)

def NthFibonacci(n):
    getNthFibSeq = [0, 1]
    while len(getNthFibSeq) < n:
        getNthFibN = getNthFibSeq[-1] + getNthFibSeq[-2]
        getNthFibSeq.append(getNthFibN)
    return getNthFibSeq
"""
    

"""def NthFibonacci1(n):
    getNthFibSeq2 = [0, 1]
    while len(getNthFibSeq2) < n:
        getNthFibN2 = getNthFibSeq2[-1] + getNthFibSeq2[-2]
        getNthFibSeq2.append(getNthFibN2)
    return getNthFibSeq2[-1]
"""

"""NthFibResult = NthFibonacci(n)
#NthFibResult1 = NthFibonacci1(n)
print(NthFibResult[-1], '//', NthFibResult) """



print('Nth Fibonacci')
n = int(input('n: '))

def NthFibonacci(n):
    fibSeq = [0, 1]
    while len(fibSeq) < n:
        nthFib = fibSeq[-1] + fibSeq[-2]
        fibSeq.append(nthFib)
    return fibSeq

fibResult = NthFibonacci(n)
print(fibResult[-1], '//', fibResult)
print('-'*15)
print("The last two Fibonacci Numbers are '{}' and '{}' respectively. ".format(fibResult[-2],fibResult[-1]))