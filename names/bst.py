class BSTNode:
    def __init__(self, value):
        #current node's value
        self.value = value
        #less than value
        self.left = None
        #greater than value
        self.right = None

    #Insert the given value into the tree
    def insert(self, value):
        #check if new node's value is less than current node's value. 
        if value < self.value:
            if not self.left: #there is no self.left
                self.left = BSTNode(value) #now making a node (not empty)
            else:
                self.left.insert(value) #inserting value
        #check whether new node's value is greater than or equal to the current's node's value
        if value >= self.value:
            if not self.right: #there is no self.right
                self.right = BSTNode(value) #creating a node 
            else:
                self.right.insert(value) #inserting the value
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check whether current node matches target. 
        if self.value == target:
            return True
        # is the target lower than the value?
        if target < self.value:
            #is there any child node?
            if not self.left:
                return False
            #if there is a node on the right, start the function over. 
            else:
                return self.left.contains(target)
        else:
            #is there any child node?
            if not self.right:
                return False
            else:
                return self.right.contains(target)