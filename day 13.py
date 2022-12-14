
# returns bool(finished), bool(left is smaller)
def compare(left, right):
	if type(left) is int and type(right) is list:
		return compare([left], right)
	if type(left) is list and type(right) is int:
		return compare(left, [right])
	if type(left) is int and type(right) is int:
		return left != right, left < right
	if type(left) is list and type(right) is list:
		l = [f for f in left]
		r = [f for f in right]
		if len(l) == 0 and len(r) > 0:
			return True, True
		if len(l) > 0 and len(r) == 0:
			return True, False
		if len(l) == 0 and len(r) == 0:
			return False, False
		l_new, r_new = l.pop(0), r.pop(0)
		fin, cor = compare(l_new, r_new)
		if not fin:
			return compare(l, r)
		return fin, cor


def one():
	data = [f.strip() for f in open("day 13 data.txt")]
	pairs = []
	for i in range(0, len(data), 3):
		pairs.append([eval(data[i]), eval(data[i + 1])])
		
	total = 0
	index = 1
	for pair in pairs:
		_, cor = compare(pair[0], pair[1])
		if cor:
			total += index
		index += 1
	return total


def insert(bef, packet):
	ret = [f for f in bef]
	index = 0
	while index < len(ret) and compare(ret[index], packet)[1]:
		index += 1
	ret.insert(index, packet)
	return ret


def insertion_sort(packets):
	ret = [packets[0]]
	for packet in packets[1:]:
		ret = insert(ret, packet)
	return ret


def two():
	data = [f.strip() for f in open("day 13 data.txt")]
	packets = []
	for i in range(0, len(data), 3):
		packets.append(eval(data[i]))
		packets.append(eval(data[i + 1]))
	packets.append([[2]])
	packets.append([[6]])
	packets = insertion_sort(packets)
	return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


print(one())
print(two())
