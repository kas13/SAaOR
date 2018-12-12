#G = [[[1,5], [2,3]],[[2,3],[3,3]],[[4, 5]],[[2,4],[4,7]],[[]]]
G = [[[1,50]],[[3,30],[2,20]],[[5, 19]],[[4,31]],[[0,10]]]
D = []
U = []



def dfs(t):
	stack = []
	stack.append(G[0])
	min_flow = 100
	path = []

	while stack != []:
		node = stack.pop()
		print("node ", node)
		for edge in node:
			print("  edge   ", edge)
			if edge[0] == t:
				print("victori")
				path.append(edge[0])
				print(path, min_flow)
				return path, min_flow
			if U[edge[0]] is True:
				continue
			elif edge[1] > edge[2]:
				U[edge[0]] = True
				stack.append(G[edge[0]])
				print("append ",G[edge[0]] )
				path.append(edge[0])
				if min_flow > edge[1] - edge[2]:
					min_flow = edge[1] - edge[2]



def recovery_path(temp_path, min_flow, t):
	print(min_flow)
	print(temp_path)
	s = 0
	path = []
	while s != t:
		prev = 0
		for road in temp_path:
			for edge in G[prev]:
				if road == edge[0]:
					if min_flow <= edge[1] - edge[2]:
						s = road
						path.append(s)
						prev = road
						#print("if")
					else:
						print("else")
						temp_path.remove(prev)
	print(path)





def main():
	n = 6
	t = 5
	global U, G
	#add flow to graph
	for node in G:
		for edge in node:
			edge.append(0)

	U = [False] * n
	temp_path, min_flow = dfs(t)
	recovery_path(temp_path, min_flow, t)

if __name__ == "__main__":
	main()