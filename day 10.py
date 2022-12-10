
def noop(x_val, total, cycle):
	if cycle % 40 == 19:
		return total + x_val * (cycle + 1), cycle + 1
	return total, cycle + 1


def add_x(x_val, add_val, total, cycle):
	if cycle % 40 == 19:
		return x_val + add_val, total + x_val * (cycle + 1), cycle + 2
	if (cycle + 1) % 40 == 19:
		return x_val + add_val, total + x_val * (cycle + 2), cycle + 2
	return x_val + add_val, total, cycle + 2


def one():
	data = [f.strip() for f in open("day 10 data.txt")]
	x_val = 1
	total = 0
	cycle = 0
	for line in data:
		if line[0] == 'n':
			total, cycle = noop(x_val, total, cycle)
		if line[0] == 'a':
			x_val, total, cycle = add_x(x_val, int(line[5:]), total, cycle)
	return total


def two():
	data = [f.strip() for f in open("day 10 data.txt")]
	x_val = 1
	lines = []
	line = ""
	cycle = 1
	while len(data) != 0:
		print("cycle:", cycle, "   x_val:", x_val)
		if (cycle - 1) in [x_val - 1, x_val, x_val + 1]:
			line += '#'
		else:
			line += ' '
		if cycle % 40 == 0:
			cycle = 0
			lines.append(line)
			line = ""
		if data[0][0] == 'n':
			data.pop(0)
		elif data[0][0] == 'a':
			data[0] = data[0][5:]
		else:
			x_val += int(data.pop(0))
		cycle += 1
	for line in lines:
		print(line)
	return lines


print(one())
print(two())
