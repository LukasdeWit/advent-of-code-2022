
def is_visible(forest, x, y):
	# left
	vis_left = True
	for i in range(x - 1, -1, -1):
		if forest[y][i] >= forest[y][x]:
			vis_left = False
	# right
	vis_right = True
	for i in range(x + 1, len(forest[0]), 1):
		if forest[y][i] >= forest[y][x]:
			vis_right = False
	# up
	vis_up = True
	for i in range(y - 1, -1, -1):
		if forest[i][x] >= forest[y][x]:
			vis_up = False
	# down
	vis_down = True
	for i in range(y + 1, len(forest), 1):
		if forest[i][x] >= forest[y][x]:
			vis_down = False
	return vis_up or vis_down or vis_left or vis_right


def one():
	data = [f.strip() for f in open("day 8 data.txt")]
	forest = []
	for point in data:
		forest.append([int(n) for n in point])
	total = 0
	for y in range(len(forest)):
		for x in range(len(forest[0])):
			if is_visible(forest, x, y):
				total += 1
	return total


def scene_score(forest, x, y):
	# left
	vis_left = 0
	for i in range(x - 1, -1, -1):
		vis_left += 1
		if forest[y][i] >= forest[y][x]:
			break
	# right
	vis_right = 0
	for i in range(x + 1, len(forest[0]), 1):
		vis_right += 1
		if forest[y][i] >= forest[y][x]:
			break
	# up
	vis_up = 0
	for i in range(y - 1, -1, -1):
		vis_up += 1
		if forest[i][x] >= forest[y][x]:
			break
	# down
	vis_down = 0
	for i in range(y + 1, len(forest), 1):
		vis_down += 1
		if forest[i][x] >= forest[y][x]:
			break
	return vis_up * vis_down * vis_left * vis_right


def two():
	data = [f.strip() for f in open("day 8 data.txt")]
	forest = []
	for point in data:
		forest.append([int(n) for n in point])
	total = 0
	for y in range(len(forest)):
		for x in range(len(forest[0])):
			total = max(total, scene_score(forest, x, y))
	return total


print(one())
print(two())
