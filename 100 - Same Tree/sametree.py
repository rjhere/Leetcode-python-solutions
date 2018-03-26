class Solution(object):
	def isSameTree(self, p, q):
		if p is None and q is None:
			return True
		elif p is None or q is None:
			return False
		elif p.val != q.val:
			return False
		else:
			return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
	None