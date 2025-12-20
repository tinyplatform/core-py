from typing import Any, Callable
from Element import Element, CompositeInterface
from Group import Group
from Property import Property
from json import dumps

class Config(CompositeInterface):
    """Top-level configuration class.
    The direct children of a config must have their parents set to None to keep simple full paths!
    """

    def __init__(self, file_path: str|None = None):
        self._file_path = file_path
        self._children: list[Element] = []
        ... # TODO

    def add_child(self, element: Element):
        if not isinstance(element, Element):
            raise TypeError(self, element)

        if element in self._children:
            raise ValueError(self, element)

        self._children.append(element)
        element._parent = None

    def has_child(self, element: Element):
        return element in self._children
    
    def query_children(self, lookup: Callable[[Element], bool]) -> list[Element]:
        matches = []
        for child in self._children:
            if lookup(child):
                matches.append(child)

        return matches
    
    def get_from_path(self, path: str) -> Element:
        for child in self._children:
            prefix = f'{child.full_path()}/'
            if child.full_path() == path:
                return child
            elif path.startswith(prefix):
                if not isinstance(child, CompositeInterface):
                    raise TypeError(self, path, child)
                
                return child.get_from_path(path.removeprefix(prefix))
        
        raise ValueError(self, path)
    
    def get_group(self, path: str) -> Group:
        child = self.get_from_path(path)

        if not isinstance(child, Group):
            raise TypeError(self, path, child)

        return child

    def get_property(self, path: str) -> Property:
        child = self.get_from_path(path)

        if not isinstance(child, Property):
            raise TypeError(self, path, child)
        
        return child

    def remove_child(self, element: Element):
        if not isinstance(element, Element):
            raise TypeError(self, element)
        
        if element not in self._children:
            raise ValueError(element)

        self._children.remove(element)
        element._parent = None

    def dump(self) -> dict[str, Any]:
        children = {}
        for child in self._children:
            children[child.name] = child.dump()
        
        return children

    def serialize(self) -> str:
        return dumps(self.dump())