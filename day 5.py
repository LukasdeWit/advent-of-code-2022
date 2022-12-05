
def parse(data):
	index = data.index('')
	field = parse_field(data[:index])
	instructions = data[index + 1:]
	return field, instructions


def parse_field(data):
	data.reverse()
	field = {}
	for num in data[0].strip().split(' '):
		field[num] = []
	for line in data[1:]:
		bites = [line[i:i+4] for i in range(0, len(line), 4)]
		for i in range(len(bites)):
			if bites[i][0] == '[':
				field[str(i + 1)].append(bites[i][1])
	return field


def one():
	data = [f.strip('\n') for f in open("day 5 data.txt")]
	field, instructions = parse(data)
	for i in instructions:
		nums = i.replace("move", '').replace("from", '').replace("to", '').split(' ')
		while '' in nums:
			nums.remove('')
		for _ in range(int(nums[0])):
			temp = field[nums[1]].pop()
			field[nums[2]].append(temp)
	ans = ''
	for i in range(1, 10):
		ans += field[str(i)].pop()
	return ans


def two():
	data = [f.strip('\n') for f in open("day 5 data.txt")]
	field, instructions = parse(data)
	for i in instructions:
		nums = i.replace("move", '').replace("from", '').replace("to", '').split(' ')
		while '' in nums:
			nums.remove('')
		for k in range(int(nums[0])):
			temp = field[nums[1]].pop(len(field[nums[1]]) - int(nums[0]) + k)
			field[nums[2]].append(temp)
	ans = ''
	for i in range(1, 10):
		ans += field[str(i)].pop()
	return ans


print(one())
print(two())
