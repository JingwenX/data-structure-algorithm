"""
596. Minimum Subtree
Description
https://www.lintcode.com/problem/minimum-subtree/description
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Have you met this question in a real interview?  
Example
Example 1:

Input:
     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 

Output:1
Example 2:

Input:
   1
Output:1
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        # set up global variable
        self.min_weight = sys.maxsize
        self.min_root = None
        self.helper(root)
        return self.min_root
        
    def helper(self, root):
        """
        @return: the weight of the subtree
        """
        if root is None:
            return 0
        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        root_weight = left_weight + right_weight + root.val
        
        # compare with the current min to update †he current min_weight
        if root_weight < self.min_weight:
            self.min_weight = root_weight
            self.min_root = root
        return root_weight