class LIS:
	""" A class for the implentation of the longest increasing 
	subsequence(LIS) algorithm using a dynamic programming appproach.

	Attributes:
		L : the input list
	"""

	def __init__(self, L):
		self.L = L

	def get_LIS():
		""" Obtain the longest increasing subsequence in the input list, L, 
		using a dynammic programming approach.

		Returns:
			list: a list containing the longest increasing subsequence in L.
			This could be an empty list if L is empty or it could be a list
			containing a single element when L contains a single element or
			L is in descending order(in this case the LIS would be the first
			element in L, L[0]).
		"""
		L = self.L
		n = len(L)
		# if input list has only 1 element or empty, return the 
		# single element or the empty list
		if n <= 1 :
			return L

		# Memorization array: M[i] contains the LIS from L[0] to L[i]
		M = list()
		# Base case
		M.append(list())
		M[0].append(L[0])

		LIS_index = 0
		m = 1

		for j in range(1,n):
			M.append(list())
			# look for subsets of M[j] and append them to M[j]
			for i in range(j):
				if L[j] > L[i] and (len(M[i]))+1 > len(M[j]):
					M[j] = M[i].copy()
			M[j].append(L[j])
			# keep track of where the LIS is in the memorization array 
			if len(M[j]) > m:
				m = len(M[j])
				LIS_index = j

		# LIS in L
		lis = L[LIS_index]

		return lis

		def LIS_size():
			""" Returns:
				int: the size of the LIS.
			"""
			return len(self.getLIS())
