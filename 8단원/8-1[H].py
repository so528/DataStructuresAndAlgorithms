def remove(self, p: Node) -> None:
    if self.head is not None:
        if p is self.head:        
            self.remove_first()   
        else:
            ptr = self.head
            while ptr.next is not p:
                ptr = ptr.next
                if ptr is None:    
                    return
            ptr.next = p.next
            self.current = ptr
            self.no -= 1

def remove_current_node(self) -> None:
    self.remove(self.current)

def clear(self) -> None:
    while self.head is not None:   
        self.remove_first()     
    self.current = None
    self.no = 0

def next(self) -> bool:
    if self.current is None or self.current.next is None:
        return False            
    self.current = self.current.next
    return True
