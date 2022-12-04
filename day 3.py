
scores_1 = {}
for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	scores_1[l] = ord(l) - ord('A') + 27
for l in "abcdefghijklmnopqrstuvwxyz":
	scores_1[l] = ord(l) - ord('a') + 1


def make_backpacks_1(line):
	return line[:len(line)//2], line[len(line)//2:]


def one():
	data = [f.strip() for f in open("day 3 data.txt")]
	total = 0

	for d in data:
		left, right = make_backpacks_1(d)
		double_letter = ''
		for l in left:
			if l in right:
				double_letter = l
		total += scores_1[double_letter]

	return total


def two():
	data = [f.strip() for f in open("day 3 data.txt")]
	total = 0

	for i in range(0, len(data), 3):
		double_letter = ''
		for l in data[i]:
			if l in data[i + 1] and l in data[i + 2]:
				double_letter = l
		total += scores_1[double_letter]

	return total


print(one())
print(two())
