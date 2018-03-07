# coding:utf-8

"""
# 0 00 空白
# 1 01 黒
# 2 10 白
# 3 11 置く場所

point_statuses = ["00", "01", "10"]


def make_next_row_dir():
	for i1 in point_statuses:
		for i2 in point_statuses:
			for i3 in point_statuses:
				for i4 in point_statuses:
					for i5 in point_statuses:
						for i6 in point_statuses:
							for i7 in point_statuses:
								for put_point in range(8):
									row_list = [i1, i2, i3, i4, i5, i6, i7]
									row_list.insert(put_point "11")
									int("".join(row_list), 2)



def retrun_next_rows(row_list, put_point):
	
	ans_list = ()
	put_point_color = "01"

def return_end_row(row_list, put_point, put_point_color):
	left_row = row_list[put_point - 1::-1]
	can_upset = False
	end_point_left = 0
	for compare_point, compare_value in enumerate(left_row):
		if compare_value == "00":
			break
		elif not compare_value == put_point_color:
			can_upset = True
			continue
		elif can_upset:
			end_point_left = compare_point -1
			break
		else:
			break

	right_row = row_list[put_point::1]
	can_upset = False
	end_point_right = 1
	for compare_point, compare_value in enumerate(right_row):
		if compare_point = 0:
			continue
		elif compare_value == "00":
			break
		elif not compare_value == put_point_color:
			can_upset = True
			continue
		elif can_upset:
			end_point_right = compare_point
			break
		else:
			break
	row_list[:put_point - end_point_left] + []

"""


import numpy as np

firld = np.zeros((10,10), "int64")
firld[0] = 9
firld[9] = 9
firld[:,0] = 9
firld[:,9] = 9
firld[4][4] = 1
firld[4][5] = 2
firld[5][4] = 2
firld[5][5] = 1

row_names = ["A", "B", "C", "D", "E", "F", "G", "H"]
replace_dict = {0: " ", 1: "*", 2: "O", 9: ""}
direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def print_firld(now_firld):
	print(" 12345678")
	for row, row_name in zip(now_firld[1:9], row_names):
		print(row_name, end="")
		for point in row:
			print(replace_dict[point], end="")
		print()


def func_input():
	print("your turn:", end="")
	put_point = input()
	if put_point == "pass":
		return None
	else:
		return (row_names.index(put_point[0]) + 1, int(put_point[1]))


def reverse(now_firld, my_color):
	put_point = func_input()
	now_firld_copy = now_firld
	now_firld_copy[put_point] = my_color
	for dx, dy in direction:
		x = put_point[0] + dx
		y = put_point[1] + dy
		if not now_firld_copy[x, y] == 3 - my_color:
			continue
		else:
			temp = []
			while now_firld_copy[x, y] == 3 - my_color:
				temp.append([x, y])
				x += dx
				y += dy
			if now_firld_copy[x, y] == my_color:
				for x, y in temp:
					now_firld_copy[x, y] = my_color
	return now_firld_copy


def can_reverse_points(now_firld, my_color):
	now_firld_copy = now_firld
	can_put_point = {None}
	for px in range(1,9):
		for py in range(1,9):
			if now_firld_copy[px, py] == 0:
				temp = []
				for dx, dy in direction:
					x = px + dx
					y = py + dy
					if not now_firld_copy[x, y] == 3 - my_color:
						continue
					else:
						
						while now_firld_copy[x, y] == 3 - my_color:
							temp.append([x, y])
							x += dx
							y += dy
						if now_firld_copy[x, y] == my_color:
							can_put_point.add((px, py))
	return can_put_point


def print_can_put_points(now_firld, my_color):
	can_put_point = can_reverse_points(now_firld, my_color)
	can_put_point.remove(None)
	for x, y in can_put_point:
		print(f"{row_names[x - 1]}{y}", end=" ")
	print()


def main():
	now_firld = firld
	while True:
		print_firld(now_firld)
		print_can_put_points(now_firld, 1)
		now_firld = reverse(now_firld, 1)

		print_firld(now_firld)
		print_can_put_points(now_firld, 2)
		now_firld = reverse(now_firld, 2)
		
if __name__ == "__main__":
	main()
