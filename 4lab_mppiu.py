start_table = [[0, 1, 2, 3, 4, 5],
               [0, 0, 1, 2, 4, 7],
               [0, 2, 2, 3, 3, 5]]

profit_table = []
resources_table = []

def bellman(n):
	profit_table.append(start_table[0])
	resources_table.append(start_table[0])
	i_array = []

	for i in range(1, len(start_table)):
		b_arr = []
		res_arr = []
		for y in range(0, n):
			by = []
			for z in range(0, y+1):
				by.append(start_table[i][z] + profit_table[i-1][y-z])
			if not by:
				b_arr.append(0)
			else:
				max_index = by.index(max(by))
				b_arr.append(max(by))
				res_arr.append(max_index)
		profit_table.append(b_arr)
		resources_table.append(res_arr)
	print(resources_table)
			
			
def find_opt_resources():
	res = len(start_table[0])
	processes_dict = {}
	for z in range(len(start_table)):
		print(profit_table)
		max_profit_row = max(profit_table)
		max_profit = max(max_profit_row)
		row = profit_table.index(max_profit_row)
		column = profit_table[row].index(max_profit)
		res_for_max = resources_table[row][column]
		res = res - res_for_max
		processes_dict[row+1] = res_for_max
		profit_table[row] = [-1] * len(start_table[0])
		for i in range(0, len(start_table)):
			for j in range(res, len(start_table[0])):
				profit_table[i][j] = -1
	print(processes_dict)


def main():
	print(bellman(len(start_table[0])))
	find_opt_resources()




if __name__ == "__main__":
	main()