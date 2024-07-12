from typing import Any
from collections import deque

class Stack:

    def __init__(self, maxlen:int=256) -> None:
        self.capacity = maxlen
        self.stk = deque([], maxlen)

    def __len__(self) -> int:
        return len(self.stk)
    
    def is_empty(self) -> bool:
        return not self.stk
    
    def is_full(self) -> bool:
        return self.stk == self.stk.maxlen
    
    def push(self, value:Any) -> None:
        self.stk.append(value)
    
    def pop(self) -> Any:
        return self.stk.pop()
    
    def peek(self) -> Any:
        return self.stk[-1]
    
    def clear(self) -> None:
        self.stk.clear()

    def find(self, value:Any) -> Any:
        try:
            return self.stk.index(value)
        except ValueError:
            return -1
    
    def count(self, value:Any) -> int:
        return self.stk.count(value)
    
    def __contains__(self, value:Any) -> bool:
        return self.count(value)
    
    def dump(self) -> int:
        print(list(self.stk))