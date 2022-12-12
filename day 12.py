
def lookup(n, tab={}):
	return tab[n]


def one():
	data = [f.strip() for f in open("day 12 data.txt")]
	vals = {}
	graph = {}
	start = ''
	end = ''
	
	# generate height map
	for j in range(len(data)):
		for i in range(len(data[0])):
			if data[j][i] == 'S':
				vals[str([j, i])] = 1
				start = str([j, i])
			elif data[j][i] == 'E':
				vals[str([j, i])] = 27
				end = str([j, i])
			else:
				vals[str([j, i])] = ord(data[j][i]) - ord('a') + 1
			graph[str([j, i])] = []
	
	# generate travel graph
	for key in vals.keys():
		key_val = eval(key)
		for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
			key_adj = str([key_val[0] + x, key_val[1] + y])
			if key_adj in vals.keys():
				if vals[key_adj] <= vals[key] + 1:
					graph[key].append(key_adj)
	
	# reuse vals for second part
	for key in vals.keys():
		vals[key] = 100000000
	
	# dijkstra's directed
	unvisited = [f for f in vals.keys()]
	queue = []
	vals[start] = 0
	current = start
	while current != end:
		unvisited.remove(current)
		for neig in graph[current]:
			if neig in unvisited:
				vals[neig] = min(vals[neig], vals[current] + 1)
				if neig not in queue:
					queue.append(neig)
		current = min(queue, key=vals.get)
		queue.remove(current)
	return vals[end]
		
	
def two():
	data = [f.strip() for f in open("day 12 data.txt")]
	vals = {}
	graph = {}
	start = ''
	end = ''
	
	# generate height map
	for j in range(len(data)):
		for i in range(len(data[0])):
			if data[j][i] == 'S':
				vals[str([j, i])] = 1
				start = str([j, i])
			elif data[j][i] == 'E':
				vals[str([j, i])] = 27
				end = str([j, i])
			else:
				vals[str([j, i])] = ord(data[j][i]) - ord('a') + 1
			graph[str([j, i])] = []
	
	# generate travel graph
	for key in vals.keys():
		key_val = eval(key)
		for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
			key_adj = str([key_val[0] + x, key_val[1] + y])
			if key_adj in vals.keys():
				if vals[key_adj] >= vals[key] - 1:
					graph[key].append(key_adj)
	
	# create nums for second part
	nums = {}
	for key in vals.keys():
		nums[key] = 100000000
	
	# dijkstra's directed
	unvisited = [f for f in vals.keys()]
	queue = []
	nums[end] = 0
	current = end
	while vals[current] != 1:
		unvisited.remove(current)
		for neig in graph[current]:
			if neig in unvisited:
				nums[neig] = min(nums[neig], nums[current] + 1)
				if neig not in queue:
					queue.append(neig)
		current = min(queue, key=nums.get)
		queue.remove(current)
	return nums[current]


print(one())
print(two())
