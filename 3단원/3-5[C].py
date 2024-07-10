def search(self, key: Any) -> Any:
    """키가 key인 원소를 검색하여 값을 반환"""
    hash = self.hash_value(key)        # 검색하는 키의 해시값
    p = self.table[hash]               # 노드를 주목

    while p is not None:
        if p.key == key:               # 검색 성공
            return p.value
        p = p.next                     # 뒤쪽 노드를 주목

    return None                        # 검색 실패

def add(self, key: Any, value: Any) -> bool:
    """키가 key이고 값이 value인 원소를 추가"""
    hash = self.hash_value(key)        # 추가하는 key의 해시값
    p = self.table[hash]               # 노드를 주목

    while p is not None:
        if p.key == key:               # 추가 실패
            return False
        p = p.next                     # 뒤쪽 노드를 주목

    temp = Node(key, value, self.table[hash])
    self.table[hash] = temp            # 노드를 추가
    return True                        # 추가 성공

