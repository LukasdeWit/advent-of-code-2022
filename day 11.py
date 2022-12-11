class Monkey:
	def __init__(self, items, operation, test_div, test_true, test_false):
		self.items = items
		self.operation = operation
		self.test_div = test_div
		self.test_true = test_true
		self.test_false = test_false
		self.activity = 0
	
	def __str__(self):
		return (f"items: {self.items}, operation: {self.operation}, test if div by {self.test_div}"
				f"- true: {self.test_true}, false: {self.test_false}, activity: {self.activity}\n")
	
	def observe(self, ex):
		self.activity += 1
		old = self.items[0]
		new = eval(self.operation)
		if ex == 1:
			self.items[0] = new // 3
		if ex == 2:
			global total_mod
			self.items[0] = new % total_mod
		if self.items[0] % self.test_div == 0:
			return self.test_true, self.items.pop(0)
		return self.test_false, self.items.pop(0)


def parse_monkey(s_monkey):
	items = eval('[' + s_monkey[1][15:] + ']')
	operation = s_monkey[2][16:].strip()
	test_div = int(s_monkey[3][19:])
	test_true = int(s_monkey[4][25:])
	test_false = int(s_monkey[5][26:])
	return Monkey(items, operation, test_div, test_true, test_false)


def one():
	data = [f.strip() for f in open("day 11 data.txt")]
	monkeys = []
	for i in range(0, len(data), 7):
		monkeys.append(parse_monkey(data[i:i + 6]))
	for i in range(20):
		for mon in monkeys:
			while not len(mon.items) == 0:
				target, item = mon.observe(1)
				monkeys[target].items.append(item)
	acts = [mon.activity for mon in monkeys]
	acts.sort()
	return acts[-1] * acts[-2]


total_mod = 1


def two():
	data = [f.strip() for f in open("day 11 data.txt")]
	monkeys = []
	for i in range(0, len(data), 7):
		monkeys.append(parse_monkey(data[i:i + 6]))
	global total_mod
	for mon in monkeys:
		total_mod *= mon.test_div
	for i in range(10000):
		for mon in monkeys:
			while not len(mon.items) == 0:
				target, item = mon.observe(2)
				monkeys[target].items.append(item)
	acts = [mon.activity for mon in monkeys]
	acts.sort()
	return acts[-1] * acts[-2]


print(one())
print(two())
