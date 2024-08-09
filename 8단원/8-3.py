# 커서로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    def __init__(self, data = None, next = None, dnext = None):
        self.data = data        # 데이터
        self.next = next        # 리스트의 뒤쪽 포인터
        self.dnext = dnext      # 프리 리스트의 뒤쪽 포인터

class ArrayLinkedList:
    """연결 리스트 클래스(배열 커서 버전)"""
    
    def __init__(self, capacity: int):
        """초기화"""
        self.head = None        # 머리 노드
        self.current = None     # 주목 노드
        self.max = None         # 사용 중인 꼬리 레코드
        self.deleted = None     # 프리 리스트의 머리 노드
        self.capacity = capacity # 리스트의 크기
        self.n = [Node()] * self.capacity # 리스트 본체
        self.no = 0             # 리스트의 현재 크기
        
    def __len__(self) -> int:
        """연결 리스트의 노드 수를 반환"""
        return self.no

    def get_insert_index(self) -> int:
        """다음에 삽입할 레코드의 인덱스를 구함"""
        if self.deleted is None:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max        # 새 레코드를 사용
            else:
                return None            # 크기 초과
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext # 프리 리스트에서 맨 앞 rec를 꺼내기
            return rec

    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트에 등록"""
        if self.deleted is None:
            self.deleted = idx
            self.n[idx].dnext = None
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec    # idx를 프리 리스트의 맨 앞에 삽입

    def add_first(self, data: Any) -> None:
        """머리 노드에 삽입"""
        ptr = self.head
        rec = self.get_insert_index()
        if rec is not None:
            self.head = self.current = rec
            self.n[self.head].data = data
            self.n[self.head].next = ptr
            self.no += 1

    def add_last(self, data: Any) -> None:
        """꼬리 노드에 삽입"""
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next is not None:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()
            if rec is not None:
                self.n[ptr].next = self.current = rec
                self.n[rec].data = data
                self.n[rec].next = None
                self.no += 1

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        if self.head is not None:
            if self.n[self.head].next is None:  # 노드가 1개뿐이면
                self.remove_first()             # 머리 노드를 삭제
            else:
                ptr = self.head
                pre = self.head
                while self.n[ptr].next is not None:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = None         # pre는 삭제한 뒤의 꼬리 노드
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """레코드 p를 삭제"""
        if self.head is not None:
            if p == self.head:               # p가 머리 노드면 머리 노드를 삭제
                self.remove_first()
            else:
                ptr = self.head
                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr is None:          # p는 리스트에 존재하지 않음
                        return
                self.n[ptr].next = None
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)
    
    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:
            self.remove_first()
        self.current = None

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.n[self.current].next is None:
            return False
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current is None:
            print("주목 노드가 없습니다.")
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head
        while ptr is not None:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """모든 레코드를 덤프"""
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def search(self, data: Any) -> int:
        """data가 포함되어 있는지 확인"""
        cnt = self.head
        while cnt is not None:
            if self.n[cnt].data == data:
                return cnt
            cnt = self.n[cnt].next
        return None

    def __iter__(self) -> 'ArrayLinkedListIterator':
        """이터레이터를 반환"""
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    """클래스 ArrayLinkedList의 이터레이터용 클래스"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> 'ArrayLinkedListIterator':
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
