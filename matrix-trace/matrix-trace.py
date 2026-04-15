def matrix_trace(A):
    total=0
    n=len(A)
    for i in range(n): 
        
        total+=A[i][i]
    return total
