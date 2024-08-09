def remove_first(self) -> None:
    if self.head is not None:
        self.head = self.currnet = self.head.next
    self.no -= 1