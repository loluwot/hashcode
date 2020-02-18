with open ('d.in', 'r') as f:
	arr1 = f.readline().split(' ')
	arr2 = f.readline().split(' ')
	arr1 = [int(x) for x in arr1]
	arr2 = [int(x) for x in arr2]
	k = [[[0, []] for x in range(arr1[0]+1)] for i in range(2)]
	counter = 0
	for i in range(len(arr2)+1):
		for ii in range(arr1[0] + 1):
			if i == 0 or ii == 0:
				continue;
			elif arr2[i-1] <= ii:
				if (k [0][ii][0] >= k[0][ii-arr2[i-1]][0]+arr2[i-1]):
					k[1][ii][0] = k[0][ii][0]
					k[1][ii][1] = k[0][ii][1]
				else:
					k[1][ii][0] = k[0][ii-arr2[i-1]][0] + arr2[i-1]
					k[1][ii][1] = k[0][ii-arr2[i-1]][1] + [i-1]
			else:
				k[1][ii][0] = k[0][ii][0]
				k[1][ii][1] = k[0][ii][1]
			print(counter)
			counter = counter + 1
		del k[0]
		temp = [[0, []] for i in range (arr1[0]+1)]
		k.append(temp)

	k[0][arr1[0]][1] = [str(x) for x in k[0][arr1[0]][1]]
	print(len(k[0][arr1[0]][1]))
	print(" ".join(k[0][arr1[0]][1]))
