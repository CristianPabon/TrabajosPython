A=[1,1,1,1]
B=[2,2,2,2]
C=[3,3,3,3]

n = len(A)
sum((((A[i])*(B[i]))+C[i]) for i in range(n))+(n**2)