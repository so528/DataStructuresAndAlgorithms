from typing import Any

class FixedQueue(Exeption):
    class Empty:
        pass

    class Full(Exeption):
        pass

    def __init__(self, capacity:int) -> None:
        self.no = 0
        self.rear = 0
        self.fornt = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity
