import pytest
from longest_increasing_sub import LIS

def test_empty_list():
	L = list()
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert  lis == [] and LISobj.LIS_size() == 0

def test_single_element_getLIS():
	L = [5]
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert lis == L

def test_single_element_LIS_size():
	L = [5]
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 1

def test_all_elements_same_getLIS():
	L = [4,4,4,4,4]
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert lis == [L[0]]

def test_all_elements_same_LIS_size():
	L = [4,4,4,4,4]
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 1

def test_arbitrary_list_getLIS():
	L = [5,2,8,6,3,6,9,7]
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert lis == [2,3,6,9] 

def test_arbitrary_list_LIS_size():
	L = [5,2,8,6,3,6,9,7]
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 4

def test_increasinglist_getLIS():
	L = [1,2,3,4,5]
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert lis == L

def test_increasinglist_LIS_size():
	L = [1,2,3,4,5]
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == len(L)

def test_decreasinglist_getLIS():
	L = [5,4,3,2,1]
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert lis == [L[0]]


def test_decreasinglist_LIS_size():
	L = [5,4,3,2,1]
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 1

def test_empty_string():
	L = ""
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert  lis == [] and LISobj.LIS_size() == 0

def test_arbitrary_string_getLIS():
	L = "abdcb"
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert  lis == ['a','b','d'] 

def test_arbitrary_string_LIS_size():
	L = "abdcb"
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 3

def test_increasing_string_getLIS():
	L = "bcdef"
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert  lis == list(L) 

def test_increasing_string_LIS_size():
	L = "bcdef"
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 5

def test_decreasing_string_getLIS():
	L = "cba"
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert  lis == list(L[0]) 

def test_decreasing_string_LIS_size():
	L = "cba"
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 1

def test_upperlower_string_getLIS():
	L = "bAcaBe"
	LISobj = LIS(L)
	lis = LISobj.get_LIS()
	assert  lis == ['A','B', 'e'] 

def test_upperlower_string_LIS_size():
	L = "bAcaBe"
	LISobj = LIS(L)
	n = LISobj.LIS_size()
	assert n == 3

