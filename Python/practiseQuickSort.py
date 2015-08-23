# coding:utf-8
'''
a practise about quickSort 
'''

def quickSort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) / 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quickSort(left) + middle + quickSort(right)

#test
arr = [3,5,0,2,11,38,2,0]
print quickSort(arr)