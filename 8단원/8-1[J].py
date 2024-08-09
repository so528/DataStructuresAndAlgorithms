class LinkedListIterator:

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> 'LinkedListIterator':
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
