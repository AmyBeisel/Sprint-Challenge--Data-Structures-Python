class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #if the node is None -> do nothing
        if node is None:
            return 
        #if their are nodes:
        if node.next_node is not None:
            self.reverse_list(node.next_node, node)
             # set the pointer of the next_node to be the previous node
            node.set_next(prev)
        else:
            # set the pointer for the next_node to be the previous node from original list
            node.set_next(prev)
            # set the last node as the head of reversed list
            self.head = node


            
