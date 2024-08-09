def print_current_node(self) -> None:
    if self.current is None:
        print('주목 노드가 존재하지 않습니다.')
    else:
        print(self.current.data)

def print(self) -> None:
    ptr = self.head
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next
