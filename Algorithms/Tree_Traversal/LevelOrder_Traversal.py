# Definition for a binary tree node.
from collections import deque
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelorder_traversal(root: TreeNode) -> None:
    if not root:
        return

    q: Deque = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(node.data + "do base case here?")

        # enqueue left child
        if node.left:
            q.append(node.left)

        # enqueue right child
        if node.right:
            q.append(node.right)
