import pytest
from longest_common_sub import LCS

def test_two_emptystrings():
	X = ""
	Y = ""
	LCSobj = LCS(X,Y)
	lcs, n = LCSobj.get_LCS()
	assert lcs == "" and n == 0

def test_X_emptystring():
	X = ""
	Y = "cat"
	LCSobj = LCS(X,Y)
	lcs, n = LCSobj.get_LCS()
	assert lcs == "" and n == 0

def test_Y_emptystring():
	Y = ""
	X = "cat"
	LCSobj = LCS(X,Y)
	lcs, n = LCSobj.get_LCS()
	assert lcs == "" and n == 0

def test_symmetry():
	X = "mycat"
	Y = "yourcat"
	LCSobj1 = LCS(X,Y)
	lcs1, n1 = LCSobj1.get_LCS()
	LCSobj2 = LCS(Y,X)
	lcs2, n2 = LCSobj2.get_LCS()
	assert lcs1 == "ycat" and lcs1 == lcs2 and n1 == len("ycat") and n1 == n2 


def test_LCS_consecutive_beginning():
	X = "mylittlecat"
	Y = "mylittledog"
	LCSobj = LCS(X,Y)
	lcs, n = LCSobj.get_LCS()
	assert lcs == "mylittle" and n == len("mylittle")

def test_LCS_consecutive_end():
	X = "littlecat"
	Y = "yourcat"
	LCSobj = LCS(X,Y)
	lcs, n = LCSobj.get_LCS()
	assert lcs == "cat" and n == len("cat")


