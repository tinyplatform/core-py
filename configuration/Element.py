from typing import Any

class ElementInterface:
    def full_path(self) -> str: ...
    def dump(self) -> Any: ...
    def serialize(self) -> str: ...

class Element(ElementInterface):
    def __init__(self, parent: ElementInterface|None, name: str):
        self.parent = parent
        self.name = name

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

    def full_path(self) -> str:
        if self._parent is None:
            return self._name
        return f'{self._parent.full_path()}/{self._name}'
