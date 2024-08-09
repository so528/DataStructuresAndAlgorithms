def print_current_node(self) -> None:
    """주목 노드를 출력"""
    if self.is_empty():
        print('주목 노드는 없습니다.')
    else:
        print(self.current.data)

def print(self) -> None:
    """모든 노드를 출력"""
    ptr = self.head.next  # 더미 노드의 뒤쪽 노드
    while ptr is not self.head:
        print(ptr.data)
        ptr = ptr.next

def print_reverse(self) -> None:
    """모든 노드를 역순으로 출력"""
    ptr = self.head.prev  # 더미 노드의 앞쪽 노드
    while ptr is not self.head:
        print(ptr.data)
        ptr = ptr.prev

def next(self) -> bool:
    """주목 노드를 한 칸 뒤로 이동"""
    if self.is_empty() or self.current.next is self.head:
        return False  # 이동할 수 없음
    self.current = self.current.next
    return True

def prev(self) -> bool:
    """주목 노드를 한 칸 앞으로 이동"""
    if self.is_empty() or self.current.prev is self.head:
        return False  # 이동할 수 없음
    self.current = self.current.prev
    return True

