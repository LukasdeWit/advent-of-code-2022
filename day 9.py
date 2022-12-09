
def is_adjacent(h, t):
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if h[0] + x == t[0] and h[1] + y == t[1]:
				return True
	return False


def move_tail(h, t):
	dx, dy = 0, 0
	if not is_adjacent(h, t):
		if h[0] != t[0]:
			dx = (h[0] - t[0]) // abs(h[0] - t[0])
		if h[1] != t[1]:
			dy = (h[1] - t[1]) // abs(h[1] - t[1])
	return [t[0] + dx, t[1] + dy]


def move_up(h, t):
	h_n = [h[0], h[1] + 1]
	t_n = move_tail(h_n, t)
	return h_n, t_n


def move_down(h, t):
	h_n = [h[0], h[1] - 1]
	t_n = move_tail(h_n, t)
	return h_n, t_n


def move_left(h, t):
	h_n = [h[0] - 1, h[1]]
	t_n = move_tail(h_n, t)
	return h_n, t_n


def move_right(h, t):
	h_n = [h[0] + 1, h[1]]
	t_n = move_tail(h_n, t)
	return h_n, t_n


def one():
	data = [f.strip() for f in open("day 9 data.txt")]
	t_positions = [[0, 0]]
	t_pos = [0, 0]
	h_pos = [0, 0]
	
	for point in data:
		if point[0] == 'U':
			for i in range(int(point[2:])):
				h_pos, t_pos = move_up(h_pos, t_pos)
				if t_pos not in t_positions:
					t_positions.append(t_pos)
		if point[0] == 'D':
			for i in range(int(point[2:])):
				h_pos, t_pos = move_down(h_pos, t_pos)
				if t_pos not in t_positions:
					t_positions.append(t_pos)
		if point[0] == 'L':
			for i in range(int(point[2:])):
				h_pos, t_pos = move_left(h_pos, t_pos)
				if t_pos not in t_positions:
					t_positions.append(t_pos)
		if point[0] == 'R':
			for i in range(int(point[2:])):
				h_pos, t_pos = move_right(h_pos, t_pos)
				if t_pos not in t_positions:
					t_positions.append(t_pos)
	return len(t_positions)


def two():
	data = [f.strip() for f in open("day 9 data.txt")]
	t_positions = [[0, 0]]
	rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
	
	for point in data:
		if point[0] == 'U':
			for i in range(int(point[2:])):
				rope[0], rope[1] = move_up(rope[0], rope[1])
				for j in range(1, len(rope) - 1):
					rope[j + 1] = move_tail(rope[j], rope[j + 1])
				if rope[-1] not in t_positions:
					t_positions.append(rope[-1])
		if point[0] == 'D':
			for i in range(int(point[2:])):
				rope[0], rope[1] = move_down(rope[0], rope[1])
				for j in range(1, len(rope) - 1):
					rope[j + 1] = move_tail(rope[j], rope[j + 1])
				if rope[-1] not in t_positions:
					t_positions.append(rope[-1])
		if point[0] == 'L':
			for i in range(int(point[2:])):
				rope[0], rope[1] = move_left(rope[0], rope[1])
				for j in range(1, len(rope) - 1):
					rope[j + 1] = move_tail(rope[j], rope[j + 1])
				if rope[-1] not in t_positions:
					t_positions.append(rope[-1])
		if point[0] == 'R':
			for i in range(int(point[2:])):
				rope[0], rope[1] = move_right(rope[0], rope[1])
				for j in range(1, len(rope) - 1):
					rope[j + 1] = move_tail(rope[j], rope[j + 1])
				if rope[-1] not in t_positions:
					t_positions.append(rope[-1])
	return len(t_positions)


print(one())
print(two())
