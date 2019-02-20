def binomialCoeff(n, k): 
	C = [[0 for i in range(k+1)]for i in range(n+1)] 
for i in range(0,n+1,1): 
		for j in range(0,min(i, k)+1,1): 
		 
			if (j == 0 or j == i): 
				C[i][j] = 1

			
			else: 
				C[i][j] = C[i - 1][j - 1] + C[i - 1][j] 

	return C[n][k] 


if __name__ == '__main__': 
	n = 5
	k = 3
	print("Total number of different ways are",binomialCoeff(n - 1, k - 1)) 
	

