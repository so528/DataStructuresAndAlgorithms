def search(self, key:Any) -> Any:
    p = self.root
    while True:
        if p is None:
            return None
        if key == p.key:
            return p.value
        elif key < p.key:
            p = p.left
        else:
            p = p.right