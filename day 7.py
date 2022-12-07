
# folder shape:
# "name" : {
# 	files = []
# 	folders = {}
# }
#
# file shape:
# "file": [789, "name"]
#

folders = {}


def build_system(data):
	global folders
	folders = {"/": {"files": [], "folders": {}}}
	command = True
	cur_folder = []
	for line in data:
		if line[0] == '$':
			command = True
		
		if command:
			# all cd commands
			if line[2] == 'c':
				if line[5] == '/':
					cur_folder = ['/']
				elif line[5] == '.':
					cur_folder.pop()
				else:
					cur_folder.append(line[5:])
			# ls command
			else:
				command = False
		else:
			# dir
			if line[0] == 'd':
				add_folder(cur_folder, line[4:])
			# file
			else:
				num, name = [f for f in line.split(' ')]
				add_file(cur_folder, [int(num), name])
		

def add_folder(path, f):
	cur_folder = folders
	for fol in path[:-1]:
		cur_folder = cur_folder[fol]["folders"]
	cur_folder[path[-1]]["folders"][f] = {"files": [], "folders": {}}


def add_file(path, f):
	cur_folder = folders
	for fol in path[:-1]:
		cur_folder = cur_folder[fol]["folders"]
	cur_folder[path[-1]]["files"].append(f)


total_size = 0
smallest_size = 100000000000000000000000


def find_size(folder, req_space=100000000000000000000000):
	global total_size
	global smallest_size
	size = 0
	for i in folder["files"]:
		size += i[0]
	for fol in folder["folders"]:
		size += find_size(folder["folders"][fol], req_space)
	if size <= 100000:
		total_size += size
	if req_space <= size < smallest_size:
		smallest_size = size
	return size
	

def one():
	data = [f.strip() for f in open("day 7 data.txt")]
	build_system(data)
	find_size(folders['/'])
	return total_size


def two():
	global smallest_size
	free_space = 70000000 - find_size(folders['/'])
	smallest_size = 100000000000000000000000
	req = 30000000 - free_space
	find_size(folders['/'], req)
	return smallest_size


print(one())
print(two())
