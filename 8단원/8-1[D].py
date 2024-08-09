def add_first(self, data:Any) -> None:
    ptr = self.head
    self.head = self.current = Node(data,ptr)
    self.no += 1