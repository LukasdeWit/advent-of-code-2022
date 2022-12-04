
def embedded_within(line):
	left, right = line.split(',')
	return int(left.split('-')[0]) >= int(right.split('-')[0]) and \
		int(left.split('-')[1]) <= int(right.split('-')[1]) or \
		int(left.split('-')[0]) <= int(right.split('-')[0]) and \
		int(left.split('-')[1]) >= int(right.split('-')[1])


def one():
	data = [f.strip() for f in open("day 4 data.txt")]
	total = 0

	for d in data:
		if embedded_within(d):
			total += 1
	return total


def has_overlap(line):
	left, right = line.split(',')
	return int(left.split('-')[0]) <= int(right.split('-')[0]) and \
		int(right.split('-')[0]) <= int(left.split('-')[1]) or \
		int(left.split('-')[0]) <= int(right.split('-')[1]) and \
		int(right.split('-')[1]) <= int(left.split('-')[1]) or \
		int(right.split('-')[0]) <= int(left.split('-')[0]) and \
		int(left.split('-')[0]) <= int(right.split('-')[1]) or \
		int(right.split('-')[0]) <= int(left.split('-')[1]) and \
		int(left.split('-')[1]) <= int(right.split('-')[1])


def two():
	data = [f.strip() for f in open("day 4 data.txt")]
	total = 0

	for d in data:
		if has_overlap(d):
			total += 1
	return total


print(one())
print(two())
