# Data structure where each node refreneces the next 
# The first and last nodes are connected to each other
# Traversable in only one direction
# When the length of the array is exceeded, the oldest value is overwritten
# Useful for filters using short term historical data



class LinkedLoop:
    def __init__(self, length=0):
        if length < 0:
            length = 0
        self.list = 
        self.length = length
        self.next = Node()
        self.last = None
        last_node = self.next
        # Create a closed loop with specific length
        """for _ in range(length):
            node = Node()
            last_node.next_node = node
            last_node = node"""

        last_node.next_node = self.next

    
    def add(self, val):
        # Overwrite the oldest value in the loop
        self.last.val = val
        self.last = self.last.next_node

    def listprint(self):
        printval = self.last
        for _ in range(self.length):

        


    
"""class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node

    @property
    def val(self):
        return self.val

    @val.setter
    def val(self, val):
        self.val = val

    @property
    def next_node(self):
        return self.next_node

    @next_node.setter
    def next_node(self, node):
        self.next_node = node


list = LinkedLoop(3)
list.add(3)
list.add(1) """







