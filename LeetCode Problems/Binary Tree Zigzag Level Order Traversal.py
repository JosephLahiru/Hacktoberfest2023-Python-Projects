class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if root is None:
            return res
        LtoR = []
        RtoL = []
        LtoR.append(root)
        lefttorigh = False
        while LtoR or RtoL:
            temp = []
            if lefttorigh:
                while RtoL:
                    node = RtoL.pop()
                    temp.append(node.val)
                    if node.left:
                        LtoR.append(node.left)
                    if node.right:
                        LtoR.append(node.right)
                temp.reverse()
                res.append(temp)
                lefttorigh = False
            else:
                while LtoR:
                    node = LtoR.pop()
                    temp.append(node.val)
                    if node.right:
                        RtoL.append(node.right)
                    if node.left:
                        RtoL.append(node.left)
                res.append(temp)
                lefttorigh = True
        return res