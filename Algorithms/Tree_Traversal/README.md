# 4 Types of Tree Traversal Algorithms
### Disclaimer:
This article is made for the sole purpose of learning and taking notes. The images and article is from [Anand Parmar's Post](https://towardsdatascience.com/4-types-of-tree-traversal-algorithms-d56328450846) on Towards Data Science [website](https://towardsdatascience.com).

</br>

## Inorder Traversal
Is one of the most used variant if DFS (Depth First Search). Inorder Traversal of Binary Search Tree will always give you Nodes in sorted manner.

### Order of Steps:
1. Go to left-subtree
2. Visit Node
3. Go to right-subtree

![Inorder](https://miro.medium.com/max/500/1*bxQlukgMC9cGv_MFUllX2Q.gif)

### Code:
```python
def inorderTraversal(root: TreeNode) -> None:
	if not root:
		return

	inorderTraversal(root.left)

	print(root.data + " ")

	inorderTraversal(root.right)
```

___

</br>

## Preorder Traversal
Preorder Traversal is another variant of DFS. Where atomic operations in a recursive function, are as same as Inorder traversal but with a different order.

### Order of Steps:
1. Visit Node
2. Go to left-subtree
3. Go to right-subtree

![Preorder](https://miro.medium.com/max/500/1*UGoV21qO6N8JED-ozsbXWw.gif)

### Code:
```python
def preorderTraversal(root: TreeNode) -> None:
	if not root:
		return

	print(root.data + " ")

	preorderTraversal(root.left)
	preorderTraversal(root.right)
```

___

</br>

## Postorder Traversal
Similar goes with Postorder Traversal. Where we visit the left subtree and the right subtree before visiting the current node in recursion.

### Order of Steps:
1. Go to left-subtree
2. Go to right-subtree
3. Visit Node

![PostOrder](https://miro.medium.com/max/500/1*UGrzA4qtLCaaCiNAKZyj_w.gif)

### Code:
```python
def postorderTraversal(root: TreeNode) -> None:
	if not root:
		return

	postorderTraversal(root.left)
	postorderTraversal(root.right)

	print(root.data + " ")
```

___

</br>

## Level Order Traversal
This is a different traversal than what we have covered above. Level order traversal follows BFS(Breadth-First Search) to visit/modify every node of the tree.

As BFS suggests, the breadth of the tree takes priority first and then move to depth. In simple words, we will visit all the nodes present at the same level one-by-one from left to right and then move to the next level to visit all the nodes of that level.

![LevelOrder](https://miro.medium.com/max/500/1*2NIfAdSadsdK2rP015f6Xg.gif)

### Code:
```python
from collection import deque

def levelorderTraversal(root: TreeNode) -> None:
	if not root:
		return

    queue = deque()
	queue.append(root)

	while queue:
		node = queue.popleft()
		print(node.data + " ")

		if node.left:
			queue.append(node.left)

		if node.right:
			queue.append(node.right)
```