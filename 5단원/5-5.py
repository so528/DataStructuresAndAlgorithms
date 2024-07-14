# 스택으로 재귀 함수 구현하기

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


def recur(n:int) -> int:
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n-1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n-2
            continue
        break

x = int(input('정수를 입력하세요.:'))

recur(x)