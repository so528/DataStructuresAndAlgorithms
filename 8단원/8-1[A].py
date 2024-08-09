# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self,data:Any = None, next:Node = None):
        self.data=data
        self.next=next