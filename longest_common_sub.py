import numpy as np
class LCS:
	""" A class for the implentation of the longest common
	subsequence(LIS) algorithm using a dynamic programming appproach.

	Attributes:
		X : an input string of size n(could be an empty string).
		Y : an input string of size m(could be an empty string).
	"""

	def __init__(self, X, Y):
		self.X = X
		self.Y = Y

	def get_LCS(self):
		""" Obtain the longest common subsequence in the input strings, X and Y, 
		using a dynammic programming approach.

		Returns:
			list: the longest common subsequence in X and Y and its length. The 
			lcs of any string and an empty string is the empty string with length 0.
			Similarly, the lcs between two empty strings is the empty string with length 0.
		"""
		X = self.X
		Y = self.Y
		n = len(X)
		m = len(Y)

		M = np.zeros((n+1,m+1), dtype=np.int)

		for i in range(1,n+1):
			for j in range(1,m+1):
				if X[i-1] == Y[j-1]:
					M[i][j] = 1 + M[i-1][j-1]
				else:
					M[i][j] = max(M[i-1][j], M[i][j-1])
		print(M)
		# length of LCS is at the bottom right corner of the table
		lcs_length = M[n][m]
		i = n 
		j = m 
		lcs = ""

		# start looping from the bottom right corner of the table M
		while i > 0 and j > 0:
	   		# add character to lcs if X[i-1] = Y[j-1] 
	   		if X[i-1] == Y[j-1]: 
	   			lcs = X[i-1] + lcs
	   			# move diagonally up in the table
	   			i -= 1
	   			j -= 1

	   		# if length of the lcs increased at the previous row then go up
	   		elif M[i-1][j] > M[i][j-1]: 
	   			i -= 1
	   		# if length of lcs increased at the previous column then go left
	   		else:
	   			j -= 1

	    
		return lcs, lcs_length
