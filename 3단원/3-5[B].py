from typing import Any, Optional
import hashlib

class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity  # 초기화 누락 수정
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
