def add(self, key:Any, value:Any) -> bool:
    
    def add_node(node:Node, key:Any, value:Any) -> None:
        if key == node.key:
            return False
        elif key < node.key:
            if node.left is None:
                node.left = Node(key, value, None, None)
            else:add_node(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value, None, None)
            else:
                add_node(node.right, key, value)
        return True
    
    if self.root is None:
        self.root = Node(Key, value, None, None)
        return True
    else:
        return add_node(self.root, key, value)