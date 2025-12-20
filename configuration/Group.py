from typing import Any
from Element import Element, ElementInterface
from json import dumps

class Group(Element):
    def __init__(self, parent: Element | None, name: str):
        super().__init__(parent, name)
        self.children: list[Element] = []

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent: ElementInterface|None):
        if parent is not None and not isinstance(parent, ElementInterface):
            raise TypeError(self, parent)
        
        self._parent = parent
        if isinstance(parent, Group):
            parent.add_child(self)

    def add_child(self, element: Element):
        if not isinstance(self, Element):
            raise TypeError(self, element)

        if element in self.children:
            raise ValueError(self, element)

        self.children.append(element)
        element._parent = self

    def remove_child(self, element: Element):
        if not isinstance(self, Element):
            raise TypeError(self, element)
        
        if element not in self.children:
            raise ValueError(element)

        self.children.remove(element)
        element._parent = None

    def dump(self) -> Any:
        children = {}
        for child in self.children:
            children[child.name] = child.dump()
        
        return children

    def serialize(self) -> str:
        return dumps(self.dump())