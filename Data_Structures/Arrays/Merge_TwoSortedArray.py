# Python program to merge
# two sorted arrays

# Merge arr1[0..n1-1] and
# arr2[0..n2-1] into
# arr3[0..n1+n2-1]
def mergeArrays(arr1, arr2, n1, n2):
	arr3 = [None] * (n1 + n2)
	i = 0
	j = 0
	k = 0

	# Traverse both array
	while i < n1 and j < n2:
	
		# Check if current element
		# of first array is smaller
		# than current element of
		# second array. If yes,
		# store first array element
		# and increment first array
		# index. Otherwise do same
		# with second array
		if arr1[i] < arr2[j]:
			arr3[k] = arr1[i]
			k = k + 1
			i = i + 1
		else:
			arr3[k] = arr2[j]
			k = k + 1
			j = j + 1
	

	# Store remaining elements
	# of first array
	while i < n1:
		arr3[k] = arr1[i];
		k = k + 1
		i = i + 1

	# Store remaining elements
	# of second array
	while j < n2:
		arr3[k] = arr2[j];
		k = k + 1
		j = j + 1
	print("Array after merging")
	for i in range(n1 + n2):
		print(str(arr3[i]), end = " ")

# Driver code
arr1 = [1, 3, 5, 7]
n1 = len(arr1)

arr2 = [2, 4, 6, 8]
n2 = len(arr2)
mergeArrays(arr1, arr2, n1, n2);
