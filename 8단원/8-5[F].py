def __iter__(self) -> DoubleLinkedListIterator:
    """이터레이터를 반환"""
    return DoubleLinkedListIterator(self.head)

def __reversed__(self) -> DoubleLinkedListReverseIterator:
    """내림차순 이터레이터를 반환"""
    return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    """DoubleLinkedList의 이터레이터용 클래스"""
    
    def __init__(self, head: Node):
        self.head = head
        self.current = head.next
    
    def __iter__(self) -> DoubleLinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    """DoubleLinkedList의 내림차순 이터레이터 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data

