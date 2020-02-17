with open ('e.in', 'r') as f:
	arr1 = f.readline().split(' ')
	arr2 = f.readline().split(' ')
	arr1 = [int(x) for x in arr1]
	arr2 = [int(x) for x in arr2]
	k = [[[0, []] for x in range(arr1[0]+1)] for i in range(len(arr2)+1)]
	for i in range(len(arr2)+1):
		for ii in range(arr1[0] + 1):
			if i == 0 or ii == 0:
				continue;
			elif arr2[i-1] <= ii:
				if (k [i-1][ii][0] >= k[i-1][ii-arr2[i-1]][0]+arr2[i-1]):
					k[i][ii][0] = k[i-1][ii][0]
					k[i][ii][1] = k[i-1][ii][1]
				else:
					k[i][ii][0] = k[i-1][ii-arr2[i-1]][0] + arr2[i-1]
					k[i][ii][1] = k[i-1][ii-arr2[i-1]][1] + [i-1]
			else:
				k[i][ii][0] = k[i-1][ii][0]
				k[i][ii][1] = k[i-1][ii][1]
	k[len(arr2)][arr1[0]][1] = [str(x) for x in k[len(arr2)][arr1[0]][1]]
	print(len(k[len(arr2)][arr1[0]][1]))
	print(" ".join(k[len(arr2)][arr1[0]][1]))
