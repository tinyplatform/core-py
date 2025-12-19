class ElementInterface:
    def full_path(self): ...

class Element(ElementInterface):
    _parent: ElementInterface|None
    _name: str

    def __init__(self, parent: ElementInterface|None, name: str):
        self._parent = parent
        self._name = name

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent: ElementInterface|None):
        if parent is not None and not isinstance(parent, ElementInterface):
            raise TypeError(self, parent)
        
        self._parent = parent

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError(self, name)
    
        self._name = name