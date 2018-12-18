# G = [
# 	[[1,2], [2,3]],
# 	[[3,13], [0, 2], [2, 0]],
# 	[[3,6], [0,3], [1, 0], [4,7]],
# 	[[2, 6], [1, 13], [4,12]],
# 	[[3,12], [2, 7]]
# ]
#[0] end node number 
#[1] capacity
#[2] max flow
#[3] flow
#[4] weight

# G = [
# 	[[1, -2, 20]],
# 	[[2, 5, 13], [3, 2, 2]],
# 	[[3, -5, 9], [4, 6, 5]],
# 	[[4, 5, 12]],
# 	[[4, 0, 1]]
# ]
G = [
	[[1, 0, 30]],
	[[2, 9, 3], [3, 10, 7], [4, -1, 7], [5, 5, 20]],
	[[5, -4, 10]],
	[[2, -3, 5]],
	[[3, 2, 6], [5, 10, 10]],
	[[5, 0, 1]]
]


INF = 100000
D = []
U = []
M = []
P = dict()
S = 0
T = 5

def find_max_flow(path):
	max_flow = 10000
	prev = 0
	for road in path:
		for edge in G[prev]:
			if edge[0] == road:
				prev = edge[0]
				if max_flow > edge[2] - edge[3]:
					max_flow = edge[2] - edge[3]
	return max_flow


def add_max_flow(max_flow, path):
	global G
	prev = 0
	for road in path:
		for edge in G[prev]:
			if edge[0] == road:
				prev = edge[0]
				edge[3] += max_flow


def add_weight_edge():
	global G
	for start, node in enumerate(G):
		for edge in node:
			finish = edge[0]
			if edge[2] - edge[3] > 0:
				edge[4] = edge[1] + U[start] - U[finish]
			else:
				edge[4] = INF

	#print("added weight ", G)


def bellman():
	global G, U
	for _ in range(len(G)):
		for start, node in enumerate(G):
			for edge in node:
				finish = edge[0]
				print("U[start] + edge[1] < U[finish] ", "{} + {} < {}".format(U[start],edge[1],U[finish]))
				if U[start] + edge[1] < U[finish] and edge[2] - edge[3] > 0:
					U[finish] = U[start] + edge[1]
	print("bellman  ", U)


def dejkstra():
	global P, D, M
	D[0] = 0
	n = len(G)
	path = []
	for i in range(n):
		v = -1
		for j in range(n): # find min len in d[] and unmark u[]
			if (D[j] < D[v] or v == -1) and M[j] is False:
				v = j
		if D[v] == INF:
			break
		M[v] = True

		for j in G[v]:
			to = j[0] #node number
			l = j[4] #weight
			#print("to {}, len {}".format(to, l))
			if D[v] + l < D[to]:
				D[to] = D[v] + l
				#print("P[to] {}, V {}".format(to, v))
				if to in P:
					P[to] = v
				else:
					P[to] = v

	for j in range(1,n):
		#print("Node {}, shortest path {}  Parent: ".format(j,D[j]))
		prev_parent = ""
		for p in range(1,j+1):
			try:
				parent = P[p]
			except:
				pass
			if parent != prev_parent:
				if j == T and parent != 0:
					path.append(parent)
				#print("{}   ".format(parent))
			prev_parent = parent
	path.append(T)

	return path


def main():
	global U, G, M, D, P
	for node in G:
		for edge in node:
			edge.append(0)
			edge.append(0)
	for i in range(5):	
		U = [INF] * (len(G) + 1)
		M = [False] * (len(G) + 1)
		D = [INF] * (len(G) + 1)
		P = dict()
		U[0] = 0

		bellman()
		add_weight_edge()
		path = dejkstra()
		if path == [T]:
			break
		max_flow = find_max_flow(path)
		add_max_flow(max_flow, path)
	print("Graph ", G)

if __name__ == "__main__":
	main()

