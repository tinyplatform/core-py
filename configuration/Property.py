from typing import Any
from Element import Element

class Property(Element):
    """Base class for all configuration properties.
    Can be used as an untyped property, but it is not recommended."""
    _value: Any
    _value_type = Any

    def __init__(self, parent: Element|None, name: str, value: _value_type|None = None):
        super().__init__(parent, name)
        self.value = value

    def is_value_valid(self, value: _value_type) -> bool:
        return True

    @property
    def value(self) -> _value_type:
        return self._value

    @value.setter
    def value(self, value: _value_type):
        if self._value_type != Any and type(value) != self._value_type:
            raise TypeError(self, value)

        if not self.is_value_valid(value):
            raise ValueError(self, value)

        self._value = value

    def __str__(self) -> str:
        return f'{self.__class__.__name__}<{self._value_type.__name__}> {self.name}({repr(self.value)})'

class IntProperty(Property):
    _value_type = int
    _min: int|None
    _max: int|None

    def __init__(self, parent: Element|None, name: str, value: _value_type|None = None, min: int|None = None, max: int|None = None):
        self._min = min
        self._max = max
        super().__init__(parent, name, value)

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    def is_value_valid(self, value: _value_type) -> bool:
        if self._min is not None and value < self._min:
            return False

        if self._max is not None and value > self._max:
            return False

        return True

if __name__ == '__main__':
    prop = Property(None, "myProp")
    print(prop)

    prop.value = 3
    print(prop)

    prop._value_type = int
    print(prop)

    try:
        prop.value = 3.14
        print(prop)
    except Exception as e:
        print(e.__class__.__name__, e)

    print(Property(prop, "lambda"))

    int_prop = IntProperty(None, "intProp", 879, min=0)
    print(int_prop)

    try:
        int_prop.value = 3.14
        print(int_prop)
    except Exception as e:
        print(e.__class__.__name__, e)

    try:
        int_prop.value = -1
        print(int_prop)
    except Exception as e:
        print(e.__class__.__name__, e)