from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for x in range(1,len(a)):
        if a[x] > maximum:
            maximum = a[x]
    return maximum
