# 체인법으로 해시 함수 구현하기(Node 클래스 만들기)

from __future__ import annotation
from typing import Any, Sequence
import hashlib

class Node:
    def __init__(self, key:Any, value:Any, next:Node) -> None:
        self.key = key
        self.value = value
        self.next = next
