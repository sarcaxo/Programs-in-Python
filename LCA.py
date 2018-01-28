nodes = list()
trace = list() 



def tree_traverser(root): #LPR
    if root == None:
        return
    tree_traverser(root.left)
    tree_traverser(root.right)
    nodes.append(root.value)
    return

def trace_node(node, value):
    if node == None:
        return None
    if node.value == value:
        return [node.value]
    trace = trace_node(node.left,value)
    if trace != None:
        trace.append(node.value)
        return trace
    trace = trace_node(node.left,value)
    if trace != None:
        trace.append(node.value)
        return trace
    return

def LCA(T, value1,value2):
    trace1 = trace_node(T, value1)
    trace2 = trace_node(T, value2)
    common_ancestor = list(set(trace1) & set(trace2)).sort()
    return common_ancestor[-1] #returns the last index value
    

class Node:
    
    def __init__(self,val):
        self.value = val;
        self.right = None;
        self.left = None;
        
   
    





#driver code
T = Node(1)
T.left = Node(2)
T.left.left = Node(3)
T.left.left.left = Node(5)
T.left.right = Node(4)
T.left.right.left = Node(6)
T.left.right.right = Node(7)
T.right = Node(8)
T.right.left = Node(9)
T.right.right = Node(10)

tree_traverser(T)
print(nodes)
print(LCA(7,5))

    