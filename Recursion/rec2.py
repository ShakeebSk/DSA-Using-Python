def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')
def printNreverse(n):
    if n>0:
        print(n,end=' ')
        printNreverse(n-1)
def printNOdd(n):
    if n>0:
        printNOdd(n-1)
        print(2*n-1,end=' ')
def printNEven(n):
    if n>0:
        printNEven(n-1)
        print(2*n,end=' ')
def printNOddreverse(n):
    if n>0:
        print(2*n-1,end=' ')
        printNOddreverse(n-1)
        
def printNEvenreverse(n):
    if n>0:
        print(2*n,end=' ')
        printNEvenreverse(n-1)
        
printNOddreverse(10)
