class Node():
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
		
class Tree():
	def __init__(self):
		self.rootNode = self.createBalancedTree()
		# self.visited = [f"{node}": False for node in rootNode]
	
	def createBalancedTree(self):
		node1 = Node(1)
		node2 = Node(2, node1)
		node4 = Node(4)
		node3 = Node(3, node2, node4)
		node6 = Node(6)
		node8 = Node(8)
		node7 = Node(7, node6, node8)
		node5 = Node(5, 3, node7)
		return node5
	
	def depthFirstSearch(self, node):
		if not node:
			return
		self.depthFirstSearch(node.left)
		self.depthFirstSearch(node.right)
		print(node.value)

tree = Tree()
print(tree.rootNode.value)
print(tree.rootNode.right.value)
print(tree.rootNode.left.value)
tree.depthFirstSearch(tree.rootNode)
input()

# ©Copyrighted by Oscar-Wyatt™ 2025.