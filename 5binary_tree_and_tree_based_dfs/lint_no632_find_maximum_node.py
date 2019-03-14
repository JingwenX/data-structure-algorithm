#lint_no632 find maximum node. Not maximum subtree!!
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    jw/o: this method is totally divide and conquer
    """
    def maxNode(self, root):
        # write your code here
        max_node, _ = self.helper(root)
        return max_node
    def helper(self, root):
        """
        compare left_max_node, right_max_node and root, return the max_node and maximum
        @return max_node, maximum
        """
        if root is None:
        	# jw/b: remember to use lowest possible number in order to calculate a max
        	# return None, 0
            return None, -sys.maxsize - 1
        left_max_node, left_maximum = self.helper(root.left)
        right_max_node, right_maximum = self.helper(root.right)
        maximum = max(left_maximum, right_maximum, root.val)

        if left_maximum == maximum:
            return left_max_node, left_maximum
        if right_maximum == maximum:
            return right_max_node, right_maximum
        return root, root.val