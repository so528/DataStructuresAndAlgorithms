def search(self, data=Any) -> int:
    cnt =0
    ptr = self.head
    while ptr is not None:
        if ptr.data == data:
            return cnt
        cnt += 1
        ptr = ptr.next
    return -1

def __contains__(self, data:Any) -> bool:
    return self.search(data) >= 0

