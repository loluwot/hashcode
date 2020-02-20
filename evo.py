import random
import math
import time
class Slide:
	def __init__(self, orient, tags, index):
		self.orient = orient
		self.tags = tags
		self.index = str(index)
	def __str__(self):
		return str(self.tags)
	def combine(self, slide):
		return Slide(self.orient, self.tags.union(slide.tags), self.index + " " + slide.index)
	def combine_set(self, slide):
		self.tags = self.tags.union(slide.tags)
		self.index = self.index + " " + slide.index

class Slideshow:
	def __init__(self, arr, scores):
		self.arr = arr
		self.scores = scores
	def swap(self, ind1, ind2):
		temp = self.arr[ind1]
		self.arr[ind1] = self.arr[ind2]
		self.arr[ind2] = temp
		if (ind1 == 0):
			self.scores[ind1] = score(self.arr[ind1], self.arr[ind1+1])
		elif (ind1 == len(self.arr)-1):
			self.scores[ind1-1] = score(self.arr[ind1], self.arr[ind1-1])
		else:
			self.scores[ind1-1] = score(self.arr[ind1], self.arr[ind1-1])
			self.scores[ind1] = score(self.arr[ind1], self.arr[ind1+1])
		if (ind2 == 0):
			self.scores[ind2] = score(self.arr[ind2], self.arr[ind2+1])
		elif (ind2 == len(self.arr)-1):
			self.scores[ind2-1] = score(self.arr[ind2], self.arr[ind2-1])
		else:
			self.scores[ind2-1] = score(self.arr[ind2], self.arr[ind2-1])
			self.scores[ind2] = score(self.arr[ind2], self.arr[ind2+1])
	def swap_score_diff(self, ind1, ind2):
		sum = 0
		if (ind1 != 0):
			sum = sum + score(self.arr[ind2], self.arr[ind1-1])-self.scores[ind1-1]
		if (ind1 != len(self.arr)-1):
			sum = sum + score(self.arr[ind2], self.arr[ind1])-self.scores[ind1]
		if (ind2 != 0):
			sum += score(self.arr[ind1], self.arr[ind2-1])-self.scores[ind2-1]
		if (ind2 != len(self.arr)-1):
			sum += score(self.arr[ind1], self.arr[ind2])-self.scores[ind2]
		return sum
	def __str__(self):
		s_arr = [str(x) for x in self.arr]
		return " ".join(s_arr)
def score(tag1, tag2):
	int_len = len(tag1.tags.intersection(tag2.tags))
	return min(int_len, len(tag2.tags)-int_len, len(tag1.tags)-int_len)


with open('b.txt', 'r') as f:
	n = int(f.readline())
	horiz = []
	vert = []
	slide = []
	scores = []
	for i in range(n):
		arr = f.readline().strip('\n').split(" ")
		orient = arr[0]
		tags = set(arr[2:])
		temp = Slide(orient, tags, i)
		slide.append(temp)
		if (orient == "H"):
			horiz.append(temp)
		else:
			vert.append(temp)
	for i in range(len(slide)-1):
		scores.append(score(slide[i], slide[i+1]))
	base = Slideshow(list(slide), list(scores))
	min_time = 100000
	min_n = -1
	for j in range(1,100,5):
		n = j
		COOLING = 0.003
		start_time = time.time()
		while (sum(base.scores) < 500):
			ind1 = random.randint(0, len(base.arr)-1)
			if (round(n) == 0):
				n = 1
			for i in range(0, len(base.arr)-1, random.randint(1,round(n))):
				if (i == ind1):
					continue
				if (base.swap_score_diff(ind1, i) == 3):
					base.swap(ind1, i)
					break
			n *= 1-COOLING

			#print(sum(base.scores))
		end_time = time.time()-start_time
		if (end_time <= min_time):
			min_time = end_time
			min_n = j
		print("{}, {}".format(min_time, min_n))
