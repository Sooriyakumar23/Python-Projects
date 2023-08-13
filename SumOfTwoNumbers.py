nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 9
Dict = {}
isNotFound = True
for index, element in enumerate(nums):
	Dict[target-element] = index 
	if element in Dict.keys():
		print (Dict[element], index)
		isNotFound = False
		break
if (isNotFound):
	print ('No matching found !')