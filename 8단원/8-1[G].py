def remove_last(self):
    if self.head is not None:
        if self.head.next is None:
            self.remove_first()
        else:
            ptr = self.head
            pre = self.head 

            while ptr.next is not None:
                pre = ptr
                ptr = ptr.next

            pre.next = None
            self.current = pre
            self.no -= 1