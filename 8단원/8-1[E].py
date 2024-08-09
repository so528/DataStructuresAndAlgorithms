def add_last(self, data:Any):
    if self.head is None:
        self.add_first(data)
    else:
        ptr = self.head 
        while ptr.next is not None:
            ptr =self.next
        ptr.next = self.current = Node(data, None)
        self.no += 1