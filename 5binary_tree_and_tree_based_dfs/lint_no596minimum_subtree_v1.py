"""
596. Minimum Subtree

====
A solution using only divide and conquer
====

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
 /     /  \
0  2  -4  -5 

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

#v0.9
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

#v1.0
class Solution:
    def findSubtree(self, root):
        min_subtree, min_weight, _ = None, sys.maxsize, 0
        min_subtree, min_weight, _ = self.helper(root)
        return min_subtree
    def helper(self, root):
        """
        @return: current minimum subtree root, current minimum subtree weight, current subtree weight.
        """

        if root is None:
            return None, sys.maxsize, 0
        # recursion function that return three parameter.
        # the key is, that the return level of the three need to be the same.
        min_subtree_l, min_subtree_weight_l, subtree_weight_l = self.helper(root.left)
        min_subtree_r, min_subtree_weight_r, subtree_weight_r = self.helper(root.right)
        root_subtree_weight = subtree_weight_l + subtree_weight_r + root.val
        """
        last method: v0.9
        we are using divide and conquer to get the sum of the subtree.
        Our helper function calculate the sum of the left, sum of the right, and return the sum of the root subtree.

        This method: v1.0
        we are using divide and conquer to get the minimum of the subtree.
        Our helper function calculate the min , and return the min of left subtree, right subtree, and root subtree.
        
        """
        # if left is the min, return the left
        cur_min_subtree_weight = min(min_subtree_weight_l, min_subtree_weight_r, root_subtree_weight)
        if min_subtree_weight_l == cur_min_subtree_weight:
            return min_subtree_l, cur_min_subtree_weight, root_subtree_weight
        if min_subtree_weight_r == cur_min_subtree_weight:
            return min_subtree_r, cur_min_subtree_weight, root_subtree_weight
        if root_subtree_weight == cur_min_subtree_weight:
            return root, cur_min_subtree_weight, root_subtree_weight

#v1.1 linghu optimization
class Solution:

    def findSubtree(self, root):
        # jw/o: here you don't have to init the parameter.
        # min_subtree, min_weight, _ = None, sys.maxsize, 0
        minimum, subtree, sum = self.helper(root)
        return subtree

    def helper(self, root):
        # jw/b: remember to have a aligned return type, if you return three things.
        if root is None:
            return sys.maxsize, None, 0 # jw: using sys.maxsize, for the default value of calculating the min
        # jw/o: variable naming. please make it as simple.
        # minimum_l: minimum weight of the subtree in the left
        # subtree_l: minimum subtree in the left
        # sum_l: sum of the left subtree
        # comment: use minimum and sum could include the meaning of weight.
        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)
        
        sum = left_sum + right_sum + root.val
        if left_minimum == min(left_minimum, right_minimum, sum):
            return left_minimum, left_subtree, sum
        if right_minimum == min(left_minimum, right_minimum, sum):
            return right_minimum, right_subtree, sum
        # jw/O: After the two ifs, you don't need a third if, instead you can just return.
        # if root_subtree_weight == cur_min_subtree_weight:
        #     return root, cur_min_subtree_weight, root_subtree_weight
        return sum, root, sum
