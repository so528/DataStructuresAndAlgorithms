def remove(self, key: Any) -> bool:
    p = self.root
    parent = None
    is_left_child = True

    while True:
        if p is None:                       
            return False                    

        if key == p.key:                    
            break                           
        else:
            parent = p                      
            if key < p.key:                 
                is_left_child = True        
                p = p.left                  
            else:                           
                is_left_child = False       
                p = p.right                 

    if p.left is None:                      
        if p is self.root:
            self.root = p.right             
        elif is_left_child:
            parent.left = p.right           
        elif p.right is None:               
            if p is self.root:
                self.root = p.left          
            elif is_left_child:
                parent.left = p.left        
            else:
                parent.right = p.left       

    else:
        parent = p
        left = p.left                       
        is_left_child = True
        while left.right is not None:       
            parent = left
            left = left.right
            is_left_child = False

        p.key = left.key                    
        p.value = left.value                
        if is_left_child:
            parent.left = left.left         
        else:
            parent.right = left.left        
    return True

