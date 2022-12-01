
def make_elves(data):
	elves = []
	elf = 0
	for d in data:
		if not d == '':
			elf += int(d)
		else:
			elves.append(elf)
			elf = 0
	return elves


def one():
	data = [f.strip("\n\n") for f in open("day 1 data.txt")]
	return max(make_elves(data))


def two():
	data = [f.strip("\n\n") for f in open("day 1 data.txt")]
	elves = make_elves(data)
	elves.sort(reverse=True)
	return sum(elves[0:3])


print(one())
print(two())
