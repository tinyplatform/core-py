from typing import Any, Callable
from .Element import Element, ElementInterface, CompositeInterface
from json import dumps

class Group(Element, CompositeInterface):
    def __init__(self, parent: Element | None, name: str):
        super().__init__(parent, name)
        self._children: list[Element] = []

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
        if not isinstance(element, Element):
            raise TypeError(self, element)

        if element in self._children:
            raise ValueError(self, element)

        self._children.append(element)
        element._parent = self

    def has_child(self, element: Element):
        return element in self._children

    def query_children(self, lookup: Callable[[Element], bool]) -> list[Element]:
        matches = []
        for child in self._children:
            if lookup(child):
                matches.append(child)

        return matches

    def get_from_path(self, path: str) -> Element:
        #print('GET FROM PATH BY', self.full_path())
        for child in self._children:
            local_path = child.full_path().removeprefix(f'{self.full_path()}/')
            prefix = f'{local_path}/'
            #print(path, child, child.full_path(), local_path)
            if local_path == path:
                return child
            elif path.startswith(prefix):
                if not isinstance(child, CompositeInterface):
                    raise TypeError(self, path, child)
                
                return child.get_from_path(path.removeprefix(prefix))

        raise ValueError(self, path)

    def remove_child(self, element: Element):
        if not isinstance(element, Element):
            raise TypeError(self, element)
        
        if element not in self._children:
            raise ValueError(element)

        self._children.remove(element)
        element._parent = None

    def dump(self) -> Any:
        children = {}
        for child in self._children:
            children[child.name] = child.dump()
        
        return children

    def serialize(self) -> str:
        return dumps(self.dump())