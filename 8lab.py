G = [[[1,5], [2,2]],[[2,3],[3,3]],[[4, 5]],[[2,4],[4,7]],[[]]]
D = []
U = []


def dfs(t):
	stack = []
	stack.append(G[0])
	while not stack is False:
		print(stack[0])
		node = stack.pop()
		for edge in node:
			if edge[0] == t:
				print("victori")
				return
			if U[edge[0]] is True:
				continue
			else:
				U[edge[0]] = True
				stack.append(G[edge[0]])



def main():
	n = 5
	global U
	U = [False] * n
	dfs(4)

if __name__ == "__main__":
	main()