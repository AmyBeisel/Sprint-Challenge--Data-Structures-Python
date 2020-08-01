class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        #create a list to store items
        self.list_items = []
        #set the first index
        self.index = 0
       

    def append(self, item):
        #if the list didn't reach the full capacity
        # add item to the end of the list
        if len(self.list_items) != self.capacity:
            self.list_items.append(item)
        #if the list reached the full capacity
        else:
            #zero index will be filled with item
            self.list_items[self.index] = item
        #increase the index and limit the values it may take
        self.index = (self.index +1) % self.capacity


    def get(self):
        return self.list_items