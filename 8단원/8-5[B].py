def search(self, data: Any) -> Any:
    """data와 값이 같은 노드를 검색"""
    cnt = 0
    ptr = self.head.next  # 현재 스캔 중인 노드

    while ptr is not self.head:
        if data == ptr.data:
            self.current = ptr
            return cnt      # 검색 성공
        cnt += 1
        ptr = ptr.next      # 뒤쪽 노드에 주목
    return -1               # 검색 실패

def __contains__(self, data: Any) -> bool:
    """연결 리스트에 data가 포함되어 있는지 판단"""
    return self.search(data) >= 0
