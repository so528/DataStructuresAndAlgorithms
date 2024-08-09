class LinkedList:
    def __init__(self) -> None:
        self.no = 0
        self.head = None
        self.current = None
    
    def __len__(self) -> int:
        return self.no