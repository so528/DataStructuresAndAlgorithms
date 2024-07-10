def remove(self, key: Any) -> bool:
    """키가 key인 원소를 삭제"""
    hash = self.hash_value(key)   # 삭제할 key의 해시값
    p = self.table[hash]
    pp = None

    while p is not None:
        if p.key == key:  # key와 일치하는 노드를 발견
            if pp is None:
                self.table[hash] = p.next
            else:
                pp.next = p.next
            return True  # key 삭제 성공
        pp = p
        p = p.next
    return False  # key 삭제 실패

def dump(self) -> None:
    """해시 테이블 덤프"""
    for i in range(self.capacity):
        p = self.table[i]
        print(i, end='')
        while p is not None:
            print(f' -> {p.key} ({p.value})', end='')
            p = p.next
        print()
