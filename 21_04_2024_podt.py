if True:
	def threeWayPartition(self, array, a, b):
		# code here 
		n = len(array)
		low = 0
		mid = 0
		high = n-1
		
		while mid <= high: #iterate until done
				ai = array[mid]
				if ai < a:
						if mid != low:
								array[mid], array[low] = array[low], array[mid]
						low += 1
						mid += 1
				elif ai > b:
						array[mid] , array[high] = array[high], array[mid]
						high -= 1
				else:
						mid += 1

myar = list(map(int, "4 9 2 5 8 10 6 2 3 10 9 9 6".split()))
threeWayPartition(0, myar, 7, 8)
print(myar)