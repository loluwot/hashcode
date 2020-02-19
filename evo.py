import random


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

    def move(self, ind1, ind2):
        if (ind1 < ind2):
            if (ind2 == len(self.arr) - 1):
                self.scores.append(score(self.arr[ind2], self.arr[ind1]))
            else:
                self.scores[ind2] = score(self.arr[ind2], self.arr[ind1])
                self.scores.insert(ind2 + 1, score(self.arr[ind2 + 1], self.arr[ind1]))
            if (ind1 == 0):
                del self.scores[ind1]
            else:
                del self.scores[ind1]
                self.scores.insert(ind1, score(self.arr[ind1 - 1], self.arr[ind1 + 1]))
                del self.scores[ind1 - 1]
            self.arr.insert(ind2 + 1, self.arr[ind1])
            del self.arr[ind1]
        elif (ind2 < ind1):
            if (ind1 == len(self.arr) - 1):
                del self.scores[ind1 - 1]
            else:
                # print("{} ind1".format(ind1))
                del self.scores[ind1]
                self.scores.insert(ind1, score(self.arr[ind1 - 1], self.arr[ind1 + 1]))
                del self.scores[ind1 - 1]
            if ind2 == 0:
                self.scores.insert(0, score(self.arr[ind2], self.arr[ind1]))
            elif ind2 == len(self.arr) - 1:
                self.scores.append(score(self.arr[ind2 - 1], self.arr[ind1]))
            else:
                # print("{} ind2".format(ind2))
                self.scores[ind2] = score(self.arr[ind2], self.arr[ind1])
                self.scores.insert(ind2 + 1, score(self.arr[ind2 + 1], self.arr[ind1]))
            temp = self.arr[ind1]
            del self.arr[ind1]
            self.arr.insert(ind2 + 1, temp)

    def __str__(self):
        s_arr = [str(x) for x in self.arr]
        return " ".join(s_arr)


def score(tag1, tag2):
    int_len = len(tag1.tags.intersection(tag2.tags))
    return min(int_len, len(tag2.tags) - int_len, len(tag1.tags) - int_len)


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
    for i in range(len(slide) - 1):
        scores.append(score(slide[i], slide[i + 1]))
    base = Slideshow(list(slide), list(scores))
    last_n = [3 for x in range(4)]
    while(3 in last_n):
        ind = random.randint(0, len(base.arr) - 1)
        elem = base.arr[ind]
        max_imp = 0
        max_ind = -1
        for i in range(0, len(base.arr) - 1, random.randint(1,3)):
            temp_score = score(elem, base.arr[i]) + score(elem, base.arr[i + 1]) - base.scores[i] - base.scores[
                ind - 1] + score(base.arr[ind - 1], base.arr[ind + 1])
            if (temp_score >= max_imp):
                max_ind = i
                max_imp = temp_score
        base.move(ind, max_ind)
        print(sum(base.scores))
        del last_n[0]
        last_n.append(max_imp)

    GENERATION_SIZE = 200
    N_GENERATIONS = 10000
    generation = [Slideshow(list(base.arr), list(base.scores)) for x in range(GENERATION_SIZE)]
    SEED_SIZE = 20
    for i in range(1, GENERATION_SIZE):
        ind1 = random.randint(0, n - 1)
        ind2 = ind1 - 1
        while (ind2 == ind1 - 1):
            ind2 = random.randint(0, n - 2)
            # print("{}, {}".format(ind1, ind2))
        generation[i].move(ind1, ind2)
    generation = sorted(generation, key=lambda slide: sum(slide.scores))
    generation = generation[GENERATION_SIZE - SEED_SIZE:]
    print(generation[-1].scores)
    for i in range(N_GENERATIONS):
        new_gen = []
        # print(generation)
        for j in range(GENERATION_SIZE // SEED_SIZE - 1):
            for k in range(SEED_SIZE):
                generation.append(Slideshow(list(generation[k].arr), list(generation[k].scores)))
            # print ("--------")
            # for s in generation:
            # 	print(s)
            # print("_---------")
        for j in range(SEED_SIZE, GENERATION_SIZE):
            ind1 = random.randint(0, n - 2)
            ind2 = ind1
            while (ind2 == ind1):
                ind2 = random.randint(0, n - 2)
                # print(generation[j])
            generation[j].move(ind1, ind2)
            # print("{}, {}".format(ind1, ind2))
            # print(generation[j])
            # print(generation[j].scores)
            # print()

        generation = sorted(generation, key=lambda slide: sum(slide.scores))
        generation = generation[GENERATION_SIZE - SEED_SIZE:]
        print(sum(generation[-1].scores))
    # print(generation[-1])
