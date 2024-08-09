def add(self, data: Any) -> None:
    """주목 노드 바로 뒤에 노드를 삽입"""
    node = Node(data, self.current, self.current.next)
    self.current.next.prev = node
    self.current.next = node
    self.current = node
    self.no += 1

def add_first(self, data: Any) -> None:
    """맨 앞에 노드를 삽입"""
    self.current = self.head  # 더미 노드 head의 바로 뒤에 삽입
    self.add(data)

def add_last(self, data: Any) -> None:
    """맨 뒤에 노드를 삽입"""
    self.current = self.head.prev  # 꼬리 노드 head.prev의 바로 뒤에 삽입
    self.add(data)

