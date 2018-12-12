#G = [[[1,5], [2,3]],[[2,3],[3,3]],[[4, 5]],[[2,4],[4,7]],[[]]]
#G = [[[1,50], [2,10]],[[3,30],[2,20]],[[5, 70]],[[4,31]],[[5,10]]]
G = [[[1,44], [3,11]],[[2,89],[3,23]],[[4, 68]],[[2,24],[4,36]],[[]]]
D = []
U = []



def dfs(t):
	stack = []
	stack.append(G[0])
	min_flow = 100
	path = []

	while stack != []:
		node = stack.pop()
		#print("node ", node)
		for edge in node:
			#print("  edge   ", edge)
			if edge[0] == t:
				#print("victori")
				path.append(edge[0])
				return path
			if U[edge[0]] is True:
				continue
			elif edge[1] > edge[2]:
				U[edge[0]] = True
				stack.append(G[edge[0]])
				#print("append ",G[edge[0]] )
				path.append(edge[0])
				#print("append edge  ",edge )
	return False



def recovery_path(temp_path,t):
	#print(temp_path)
	s = 0
	while s != t:
		prev = 0
		for road in temp_path:
			if G[prev] == []:
				temp_path.remove(prev)
			else:
				possible_road = False
				for edge in G[prev]:
					#print("edge {}, road {}".format(edge, road))
					if road == edge[0]:
						#print("e1 {}, e2 {}".format(edge[1], edge[2]))
						if edge[1] > edge[2]:
							s = road
							prev = road
							possible_road = True
						if edge[1] == edge[2]:
							temp_path.remove(prev)
							#print("  edge[1] == edge[2]",temp_path, " ", prev)
							prev = temp_path[0]
							possible_road = True
							continue

				if possible_road is False:
					if prev == 0:
						return False

					#print(temp_path, " ", prev)
					temp_path.remove(prev)

	#print(temp_path)
	return temp_path


def find_min_flow(path):
	min_flow = 10000
	prev = 0
	for road in path:
		for edge in G[prev]:
			if edge[0] == road:
				prev = edge[0]
				if min_flow > edge[1] - edge[2]:
					min_flow = edge[1] - edge[2]
	return min_flow


def start_flow(min_flow, path):
	global G
	prev = 0
	for road in path:
		for edge in G[prev]:
			if edge[0] == road:
				prev = edge[0]
				edge[2] += min_flow






def main():
	n = 5
	t = 4
	global U, G
	#add flow to graph
	for node in G:
		for edge in node:
			edge.append(0)

	while True:
		U = [False] * n
		temp_path = dfs(t)
		if temp_path is False:
			return
		path = recovery_path(temp_path, t)
		if path is False:
			#print("path is false")
			return
		min_flow = find_min_flow(path)
		start_flow(min_flow, path)
		print("min {} path {}".format(min_flow, path))

if __name__ == "__main__":
	main()