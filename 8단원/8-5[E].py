def remove_current_node(self) -> None:
    """주목 노드 삭제"""
    if not self.is_empty():
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.current = self.current.prev
        self.no -= 1
        if self.current is self.head:
            self.current = self.head.next

def remove(self, p: Node) -> None:
    """노드 p를 삭제"""
    ptr = self.head.next

    while ptr is not self.head:
        if ptr is p:
            self.current = p
            self.remove_current_node()
            break
        ptr = ptr.next

def remove_first(self) -> None:
    """머리 노드 삭제"""
    self.current = self.head.next
    self.remove_current_node()

def remove_last(self) -> None:
    """꼬리 노드 삭제"""
    self.current = self.head.prev
    self.remove_current_node()

def clear(self) -> None:
    """모든 노드를 삭제"""
    while not self.is_empty():  # 리스트 전체가 빌 때까지
        self.remove_first()      # 머리 노드를 삭제
    self.no = 0
