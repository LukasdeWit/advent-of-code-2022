
wins_1 = ["A Y", "B Z", "C X"]
draws_1 = ["A X", "B Y", "C Z"]
losses_1 = ["A Z", "B X", "C Y"]
points_1 = {'X': 1, 'Y': 2, 'Z': 3}


def one():
	data = [f.strip() for f in open("day 2 data.txt")]
	score = 0
	for d in data:
		if d in wins_1:
			score += 6
		if d in draws_1:
			score += 3
		score += points_1[d[2]]
	return score


points_2 = {'X': 0, 'Y': 3, 'Z': 6}
throws_2 = {'A': 1, 'B': 2, 'C': 3}
possibles = ['A', 'B', 'C']


def two():
	data = [f.strip() for f in open("day 2 data.txt")]
	score = 0
	for d in data:
		score += points_2[d[2]]
		throw_index = possibles.index(d[0])
		if d[2] == 'Z':
			throw_index += 1
		if d[2] == 'X':
			throw_index += 2
		score += throws_2[possibles[throw_index % 3]]
	return score
		
		


print(one())
print(two())
