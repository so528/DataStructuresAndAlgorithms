from typing import Any

class FixedQueue(Exception):
    class Empty:
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity:int) -> None:
        self.no = 0
        self.rear = 0
        self.front = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def enque(self, value:Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        
        self.que[self.rear] = value
        self.rear += 1 
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        
        self.value = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return self.value
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value:Any) -> Any:
        for i in range(self.no):
            idx = (self.front + i) % self.capacity
            if self.que[idx] == value:
                return idx
            return -1
        
    def count(self, value:Any) -> int:
        c = 0
        for i in range(self.no):
            idx = (self.front + i) % self.capacity
            if self.que[idx] == value:
                c += 1
            return c 
        
    def __contains__(self, value:Any) -> bool:
        for i in range(self.no):
            idx = (self.front + i) % self.capacity
            if self.que[idx] == value:
                return True
        return False
    
    def clear(self) -> None:
        self.rear = 0
        self.front = 0

    def dump(self) -> Any:
        if self.is_empty:
            print('큐가 비었습니다.')
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(self.que[idx], end='')