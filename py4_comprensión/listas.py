A=[1,2,3,9]
B=[4,5,6,7]

n = len(A)//2
[(((A[i+1]**2)*(B[2*i]))+B[n+i]) for i in range(n)]